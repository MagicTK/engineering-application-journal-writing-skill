from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_suite", ROOT / "scripts" / "validate_suite.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

INSTALL_SPEC = importlib.util.spec_from_file_location(
    "install_suite", ROOT / "scripts" / "install_suite.py"
)
assert INSTALL_SPEC and INSTALL_SPEC.loader
INSTALLER = importlib.util.module_from_spec(INSTALL_SPEC)
INSTALL_SPEC.loader.exec_module(INSTALLER)


class SuiteValidatorTests(unittest.TestCase):
    def test_credential_markers(self) -> None:
        self.assertTrue(VALIDATOR.SECRET_RE.search('gh' + 'p_' + 'a' * 36))
        self.assertTrue(VALIDATOR.SECRET_RE.search('-----BEGIN ' + 'OPENSSH PRIVATE KEY-----'))
        self.assertFalse(VALIDATOR.SECRET_RE.search('Never publish credentials.'))

    def test_private_root_path(self) -> None:
        self.assertTrue(VALIDATOR.PRIVATE_PATH_RE.search('/' + 'root/' + 'private-project'))

    def test_current_suite_passes(self) -> None:
        self.assertEqual([], VALIDATOR.validate(ROOT))

    def test_evidence_identifiers_resolve_to_unique_sources(self) -> None:
        index = (ROOT / "references/published-evidence.md").read_text()
        source_table = index.split("## Sources /", 1)[1].split("Some source titles", 1)[0]
        identifiers = re.findall(r"^\| (P\d{2}) \|", source_table, re.M)
        self.assertTrue(identifiers)
        self.assertEqual(len(identifiers), len(set(identifiers)))
        known = set(identifiers)
        for folder in ("references", "skills", "skills-zh"):
            for path in (ROOT / folder).rglob("*.md"):
                used = set(re.findall(r"\bP\d{2}\b", path.read_text()))
                self.assertFalse(used - known, f"{path.relative_to(ROOT)}: {used - known}")

    def test_symlink_rejected_before_reading_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "suite-manifest.yaml").symlink_to(root / "missing-target")
            self.assertEqual(
                ["unreviewed symlink should not be committed: suite-manifest.yaml"],
                VALIDATOR.validate(root),
            )

    def test_evidence_count_allows_generic_links_and_history(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "references").mkdir()
            (root / "references/published-evidence.md").write_text(
                "A selected 2-paper corpus; not all 2 papers fully read. 合计2篇。\n"
                "## Sources / 来源\n| P01 | One |\n| P02 | Two |\n"
                "Some source titles\nHistorical audit used a 1-paper subset.\n"
            )
            (root / "README.md").write_text("[published evidence](references/published-evidence.md)")
            (root / "README_CN.md").write_text("[2 篇文献](references/published-evidence.md)")
            self.assertEqual([], VALIDATOR.check_evidence_counts(root))

    def test_evidence_count_rejects_stale_bilingual_navigation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "references").mkdir()
            (root / "references/published-evidence.md").write_text(
                "A selected 2-paper corpus.\n## Sources / 来源\n"
                "| P01 | One |\n| P02 | Two |\nSome source titles\n"
            )
            (root / "README.md").write_text("[1-paper index](references/published-evidence.md)")
            (root / "references/engineering-application-terminology-bank_CN.md").write_text(
                "[3 篇文献](published-evidence.md)"
            )
            issues = VALIDATOR.check_evidence_counts(root)
            self.assertEqual(2, len(issues))
            self.assertTrue(all("table has 2" in issue for issue in issues))

    def test_evidence_count_checks_scope_and_duplicate_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "references").mkdir()
            (root / "references/published-evidence.md").write_text(
                "A selected 2-paper corpus; 合计2篇。\n## Sources / 来源\n"
                "| P01 | One |\n| P01 | Copy |\nSome source titles\n"
            )
            issues = VALIDATOR.check_evidence_counts(root)
            self.assertEqual(3, len(issues))
            self.assertIn("distinct nonempty source IDs", issues[0])

    def test_comment_case_has_literal_tex_commands(self) -> None:
        for filename in (
            "v4-behavior-cases.json",
            "history/v4.0.0/forward-test-report.json",
            "history/v4.1.0/forward-test-report.json",
            "forward-test-report.json",
        ):
            payload = json.loads((ROOT / "evals" / filename).read_text())
            matches = [c for c in payload["cases"] if c["id"] == "v4-comment-lock"]
            if filename != "forward-test-report.json":
                self.assertEqual(1, len(matches), filename)
            for case in matches:
                self.assertIn(chr(92) + "iffalse", case["prompt"])
                self.assertNotIn(chr(92) * 2 + "iffalse", case["prompt"])

    def test_evidence_rejects_duplicate_doi_resolver_forms(self) -> None:
        alternatives = (
            "http://dx.doi.org/10.1000/example(part)",
            "https://DOI.ORG/10.1000/EXAMPLE(PART)?download=1#abstract",
            "https://doi.org/10.1000%2Fexample%28part%29",
            "<https://doi.org/10.1000/example(part)>",
        )
        for alternative in alternatives:
            with self.subTest(target=alternative), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                (root / "references").mkdir()
                (root / "references/published-evidence.md").write_text(
                    "A selected 2-paper corpus.\n## Sources / 来源\n"
                    "| P01 | [Original](https://doi.org/10.1000/Example(Part)) | Note |\n"
                    f"| P02 | [Another download]({alternative}) | Note |\n"
                    "Some source titles\n"
                )
                issues = VALIDATOR.check_evidence_counts(root)
                self.assertEqual(1, len(issues))
                self.assertIn("P01 and P02 share DOI", issues[0])

    def test_evidence_doi_comparison_preserves_suffix_identity(self) -> None:
        distinct_pairs = (
            ("10.1000/%C3%81", "10.1000/%C3%A1"),
            ("10.1000/part", "10.1000/part/"),
            ("10.1000/part%252Fextra", "10.1000/part%2Fextra"),
            ("10.1000/part%23tail", "10.1000/part#tail"),
        )
        for first, second in distinct_pairs:
            with self.subTest(first=first, second=second), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                (root / "references").mkdir()
                (root / "references/published-evidence.md").write_text(
                    "A selected 2-paper corpus.\n## Sources / 来源\n"
                    f"| P01 | [First](https://doi.org/{first}) | Note |\n"
                    f"| P02 | [Second](https://doi.org/{second}) | Note |\n"
                    "Some source titles\n"
                )
                self.assertEqual([], VALIDATOR.check_evidence_counts(root))

    def test_evidence_doi_check_uses_primary_citations_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "references").mkdir()
            (root / "references/published-evidence.md").write_text(
                "A selected 2-paper corpus.\n## Sources / 来源\n"
                "| P01 | [Same title](https://doi.org/10.1000/first) | [Background](https://doi.org/10.1000/second) |\n"
                "| P02 | [Same title](https://doi.org/10.1000/second) | Note |\n"
                "Some source titles\n[Repeated discussion](https://doi.org/10.1000/first)\n"
            )
            self.assertEqual([], VALIDATOR.check_evidence_counts(root))
            (root / "references/published-evidence.md").write_text(
                "A selected 2-paper corpus.\n## Sources / 来源\n"
                "| P01 | [One](https://archive.example/one) | Note |\n"
                "| P02 | [Two](https://archive.example/two) | Note |\n"
                "Some source titles\n"
            )
            self.assertEqual([], VALIDATOR.check_evidence_counts(root))

    def test_manifest_version_and_pairs(self) -> None:
        suite, records = VALIDATOR.parse_manifest(
            (ROOT / "suite-manifest.yaml").read_text(encoding="utf-8")
        )
        self.assertEqual("4.1.29", suite["version"])
        self.assertEqual("whole-suite", suite["installation"])
        self.assertEqual(14, len(records))

    def test_bilingual_invariants_match(self) -> None:
        _, records = VALIDATOR.parse_manifest(
            (ROOT / "suite-manifest.yaml").read_text(encoding="utf-8")
        )
        for record in records:
            canonical = VALIDATOR.extract_invariants(ROOT / record["canonical"])
            mirror = VALIDATOR.extract_invariants(ROOT / record["mirror"])
            self.assertTrue(canonical, record["id"])
            self.assertEqual(canonical, mirror, record["id"])

    def test_eval_case_ids_are_unique(self) -> None:
        for filename in (
            "trigger-routing.json",
            "behavior-cases.json",
            "v4-behavior-cases.json",
            "v41-behavior-cases.json",
            "forward-test-report.json",
        ):
            payload = json.loads((ROOT / "evals" / filename).read_text(encoding="utf-8"))
            ids = [case["id"] for case in payload["cases"]]
            self.assertEqual(len(ids), len(set(ids)), filename)

    def test_trigger_eval_skills_exist(self) -> None:
        _, records = VALIDATOR.parse_manifest(
            (ROOT / "suite-manifest.yaml").read_text(encoding="utf-8")
        )
        known = {record["id"] for record in records}
        known.update(f"{record['id']}-zh" for record in records)
        payload = json.loads(
            (ROOT / "evals" / "trigger-routing.json").read_text(encoding="utf-8")
        )
        for case in payload["cases"]:
            expected = case["expected_skill"]
            if expected is not None:
                self.assertIn(expected, known, case["id"])

    def test_genericity_regression_case_is_present(self) -> None:
        payload = json.loads(
            (ROOT / "evals" / "behavior-cases.json").read_text(encoding="utf-8")
        )
        cases = {case["id"]: case for case in payload["cases"]}
        self.assertIn("dependency-not-default", cases)
        self.assertIn(
            "treat a model component as the industrial problem",
            cases["dependency-not-default"]["forbidden_behaviors"],
        )

    def test_project_scenarios_preserve_complete_unique_mapping(self) -> None:
        payload = json.loads(
            (ROOT / "evals" / "behavior-cases.json").read_text(encoding="utf-8")
        )
        source_ids = [
            case["source_case_id"]
            for case in payload["cases"]
            if "source_case_id" in case
        ]
        self.assertCountEqual([f"T{index:02}" for index in range(1, 17)], source_ids)

    def test_behavior_schema_rejects_nontext_rubrics(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "behavior.json"
            for invalid in ([""], [None], ["valid", 7]):
                payload = {
                    "schema_version": 1,
                    "cases": [{
                        "id": "invalid-rubric",
                        "prompt": "Review this case.",
                        "required_behaviors": invalid,
                        "forbidden_behaviors": ["invent evidence"],
                    }],
                }
                path.write_text(json.dumps(payload), encoding="utf-8")
                self.assertIn(
                    "case invalid-rubric has invalid required_behaviors",
                    VALIDATOR.validate_eval(path, "behavior"),
                )

    def test_generic_core_keeps_method_axis_separate(self) -> None:
        root_skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        passport = (ROOT / "assets/templates/manuscript-passport.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Keep the core workflow topic-neutral", root_skill)
        self.assertIn("Primary method strategy", passport)
        self.assertIn("Excluded Default Narratives", passport)

    def test_bilingual_triggers_are_language_disjoint(self) -> None:
        _, records = VALIDATOR.parse_manifest(
            (ROOT / "suite-manifest.yaml").read_text(encoding="utf-8")
        )
        for record in records:
            canonical = VALIDATOR.parse_frontmatter(ROOT / record["canonical"])
            mirror = VALIDATOR.parse_frontmatter(ROOT / record["mirror"])
            self.assertIn("English-language requests", canonical["description"])
            self.assertIn("中文请求", mirror["description"])

    def test_evidence_profile_is_non_ordinal(self) -> None:
        taxonomy = (ROOT / "references/industrial-ai-taxonomy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Evidence codes are non-ordinal", taxonomy)
        for code in ("EA", "EB", "ER", "EP", "EO", "EX", "EV"):
            self.assertIn(f"| {code} |", taxonomy)
        passport = (ROOT / "assets/templates/manuscript-passport.md").read_text(
            encoding="utf-8"
        )
        router = (ROOT / "skills/industrial-ai-paper-router/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("Available levels", passport)
        self.assertNotIn("Required levels", passport)
        self.assertNotIn("strongest evidence", router.lower())

    def test_installer_copy_and_symlink_modes(self) -> None:
        installer = ROOT / "scripts/install_suite.py"
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            copy_target = temp_root / "copy" / "engineering-application-journal-writing-skill"
            link_target = temp_root / "link" / "engineering-application-journal-writing-skill"

            copied = subprocess.run(
                [sys.executable, str(installer), "--copy", "--target", str(copy_target)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, copied.returncode, copied.stderr)
            self.assertTrue((copy_target / "SKILL.md").is_file())
            self.assertTrue((copy_target / "references").is_dir())

            linked = subprocess.run(
                [sys.executable, str(installer), "--target", str(link_target)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, linked.returncode, linked.stderr)
            self.assertTrue(link_target.is_symlink())

    def test_installer_rejects_invalid_source_before_creating_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "new-parent" / "suite"
            for copy in (False, True):
                args = mock.Mock(target=target, copy=copy, dry_run=False)
                with mock.patch.object(INSTALLER, "parse_args", return_value=args), \
                     mock.patch.object(INSTALLER.subprocess, "run", return_value=mock.Mock(returncode=1)) as run:
                    self.assertEqual(1, INSTALLER.main())
                self.assertEqual(1, run.call_count)
                self.assertFalse(target.parent.exists())

    def test_installer_preserves_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "existing"
            target.mkdir()
            marker = target / "author-note.txt"
            marker.write_text("local changes", encoding="utf-8")
            for copy in (False, True):
                args = mock.Mock(target=target, copy=copy, dry_run=False)
                with mock.patch.object(INSTALLER, "parse_args", return_value=args), \
                     mock.patch.object(INSTALLER.subprocess, "run") as run:
                    self.assertEqual(2, INSTALLER.main())
                run.assert_not_called()
                self.assertEqual("local changes", marker.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
