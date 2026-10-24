#!/usr/bin/env python3
"""Dependency-free structural validator for the bilingual skill suite."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "suite-manifest.yaml"
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
INVARIANT_RE = re.compile(r"<!--\s*invariant:\s*([a-z0-9-]+)\s*-->")
PRIVATE_PATH_RE = re.compile(
    r"/(?:Users|home)/[^/\s]+/|/root/[A-Za-z0-9_-]+|[A-Za-z]:\\Users\\[^\\\s]+\\"
)
SECRET_RE = re.compile(
    r"\bgh[pousr]_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}"
    r"|\bsk-(?:proj-)?[A-Za-z0-9_-]{30,}"
    r"|-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
)
QUOTED_YAML_RE = re.compile(r'^\s*([a-z_]+):\s*"(.*)"\s*$')

REQUIRED_TEMPLATES = {
    "manuscript-passport.md",
    "problem-design-evidence-blueprint.md",
    "claim-evidence-matrix.md",
    "figure-table-contract.md",
    "author-handoff.md",
    "local-corpus-map.example.yaml",
}
REQUIRED_EVALS = {
    "trigger-routing.json",
    "behavior-cases.json",
    "v4-behavior-cases.json",
    "v41-behavior-cases.json",
    "forward-test-report.json",
}
REQUIRED_REPOSITORY_FILES = {
    "CONTRIBUTING.md",
    ".github/workflows/validate.yml",
    "evals/README.md",
    "scripts/install_suite.py",
}


def parse_manifest(text: str) -> tuple[dict[str, str], list[dict[str, str]]]:
    suite: dict[str, str] = {}
    records: list[dict[str, str]] = []
    section = ""
    current: dict[str, str] | None = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == "suite:":
            section = "suite"
            continue
        if line == "skills:":
            if current:
                records.append(current)
                current = None
            section = "skills"
            continue
        if section == "skills" and line.startswith("- id:"):
            if current:
                records.append(current)
            current = {"id": line.split(":", 1)[1].strip().strip('"')}
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"')
        if section == "suite" and raw.startswith("  "):
            suite[key.strip()] = value
        elif section == "skills" and current is not None:
            current[key.strip()] = value

    if current:
        records.append(current)
    return suite, records


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing closing frontmatter delimiter")
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def extract_invariants(path: Path) -> set[str]:
    return set(INVARIANT_RE.findall(path.read_text(encoding="utf-8")))


def parse_openai_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        match = QUOTED_YAML_RE.match(raw)
        if match:
            data[match.group(1)] = match.group(2)
    return data


def clean_link_target(target: str) -> str:
    target = target.split("#", 1)[0].strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def check_links(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        clean = clean_link_target(target)
        if clean and not (path.parent / clean).resolve().exists():
            issues.append(f"broken local link: {target}")
    return issues


def check_evidence_counts(root: Path) -> list[str]:
    """Check current index claims and navigation, not dated historical counts."""
    index = root / "references/published-evidence.md"
    if not index.is_file():
        return []
    text = index.read_text(encoding="utf-8")
    if "## Sources /" not in text:
        return ["published evidence index has no source table"]
    scope, table = text.split("## Sources /", 1)
    table = table.split("Some source titles", 1)[0]
    identifiers = re.findall(r"^\| (P\d{2,}) \|", table, re.M)
    count = len(set(identifiers))
    issues: list[str] = []
    if not count or count != len(identifiers):
        issues.append("published evidence index needs distinct nonempty source IDs")
    for pattern in (r"selected (\d+)-paper corpus", r"all (\d+) papers", r"合计\s*(\d+)\s*篇"):
        for claimed in re.findall(pattern, scope):
            if int(claimed) != count:
                issues.append(f"published evidence scope claims {claimed} sources; table has {count}")
    paths = [root / "README.md", root / "README_CN.md"]
    paths.extend(root.glob("references/engineering-application-terminology-bank*.md"))
    for path in paths:
        if not path.is_file():
            continue
        for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if Path(clean_link_target(target)).name != "published-evidence.md":
                continue
            match = re.search(r"(\d+)\s*(?:-paper|paper|篇)", label)
            if match and int(match.group(1)) != count:
                issues.append(f"{path.relative_to(root)}: evidence link claims {match.group(1)} sources; table has {count}")
    return issues


def validate_eval(
    path: Path, expected_kind: str, known_skills: set[str] | None = None
) -> list[str]:
    issues: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid JSON: {exc}"]
    if payload.get("schema_version") != 1:
        issues.append("schema_version must be 1")
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        return issues + ["cases must be a non-empty list"]
    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            issues.append(f"case {index} is not an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            issues.append(f"case {index} has no id")
        elif case_id in seen:
            issues.append(f"duplicate case id: {case_id}")
        else:
            seen.add(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            issues.append(f"case {case_id or index} has no prompt")
        if expected_kind == "trigger":
            if "expected_skill" not in case:
                issues.append(f"case {case_id or index} has no expected_skill")
            else:
                expected_skill = case.get("expected_skill")
                if expected_skill is not None and not isinstance(expected_skill, str):
                    issues.append(f"case {case_id or index} has invalid expected_skill")
                elif (
                    isinstance(expected_skill, str)
                    and known_skills is not None
                    and expected_skill not in known_skills
                ):
                    issues.append(
                        f"case {case_id or index} references unknown skill {expected_skill}"
                    )
        if expected_kind == "behavior":
            for field in ("required_behaviors", "forbidden_behaviors"):
                values = case.get(field)
                if (
                    not isinstance(values, list)
                    or not values
                    or any(not isinstance(value, str) or not value.strip() for value in values)
                ):
                    issues.append(f"case {case_id or index} has invalid {field}")
    return issues


def validate(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    symlinks = [
        path for path in root.rglob("*")
        if ".git" not in path.relative_to(root).parts and path.is_symlink()
    ]
    if symlinks:
        return [
            f"unreviewed symlink should not be committed: {path.relative_to(root)}"
            for path in symlinks
        ]
    manifest = root / "suite-manifest.yaml"
    if not manifest.exists():
        return ["missing suite-manifest.yaml"]

    suite, records = parse_manifest(manifest.read_text(encoding="utf-8"))
    suite_version = suite.get("version", "")
    if not suite_version:
        issues.append("manifest suite has no version")
    if suite.get("installation") != "whole-suite":
        issues.append("manifest must declare installation: whole-suite")
    if not records:
        issues.append("manifest contains no skill records")

    seen_names: set[str] = set()
    listed_skill_files: set[Path] = set()
    descriptions: dict[str, str] = {}

    for record in records:
        for field in ("id", "version", "canonical", "mirror"):
            if not record.get(field):
                issues.append(f"manifest record missing {field}: {record}")
        if any(not record.get(field) for field in ("id", "version", "canonical", "mirror")):
            continue
        if record["version"] != suite_version:
            issues.append(f"{record['id']}: version differs from suite version")

        paths: dict[str, Path] = {}
        for role in ("canonical", "mirror"):
            path = root / record[role]
            paths[role] = path
            listed_skill_files.add(path.resolve())
            if not path.exists():
                issues.append(f"missing {role} file: {path.relative_to(root)}")
                continue
            try:
                fm = parse_frontmatter(path)
            except ValueError as exc:
                issues.append(f"{path.relative_to(root)}: {exc}")
                continue
            for required in ("name", "description"):
                if not fm.get(required):
                    issues.append(f"{path.relative_to(root)}: missing {required}")
            name = fm.get("name", "")
            expected_name = record["id"] if role == "canonical" else f"{record['id']}-zh"
            if name != expected_name:
                issues.append(
                    f"{path.relative_to(root)}: expected skill name {expected_name}, found {name}"
                )
            if path != root / "SKILL.md" and path.parent.name != name:
                issues.append(
                    f"{path.relative_to(root)}: parent directory must match skill name {name}"
                )
            if name in seen_names:
                issues.append(f"duplicate skill name: {name}")
            seen_names.add(name)
            description = fm.get("description", "")
            if description in descriptions:
                issues.append(
                    f"duplicate trigger description: {path.relative_to(root)} and {descriptions[description]}"
                )
            descriptions[description] = str(path.relative_to(root))
            if len(description) < 40 or len(description) > 1200:
                issues.append(f"{path.relative_to(root)}: implausible description length")
            if role == "canonical" and "English-language requests" not in description:
                issues.append(
                    f"{path.relative_to(root)}: canonical trigger must select English-language requests"
                )
            if role == "mirror" and "中文请求" not in description:
                issues.append(
                    f"{path.relative_to(root)}: Chinese mirror trigger must select Chinese requests"
                )
            if len(path.read_text(encoding="utf-8").splitlines()) > 500:
                issues.append(f"{path.relative_to(root)}: exceeds 500 lines")

            metadata = (root / "agents/openai.yaml") if path == root / "SKILL.md" else path.parent / "agents/openai.yaml"
            if not metadata.exists():
                issues.append(f"{path.relative_to(root)}: missing agents/openai.yaml")
            else:
                ui = parse_openai_yaml(metadata)
                for key in ("display_name", "short_description", "default_prompt"):
                    if not ui.get(key):
                        issues.append(f"{metadata.relative_to(root)}: missing quoted {key}")
                if ui.get("default_prompt") and f"${name}" not in ui["default_prompt"]:
                    issues.append(f"{metadata.relative_to(root)}: default_prompt must mention ${name}")
                short = ui.get("short_description", "")
                if short and not 10 <= len(short) <= 100:
                    issues.append(f"{metadata.relative_to(root)}: short_description must be 10-100 characters")

            version_marker = (
                f'Suite version: `{record["version"]}`'
                if role == "canonical"
                else f'套件版本：`{record["version"]}`'
            )
            if version_marker not in path.read_text(encoding="utf-8"):
                issues.append(f"{path.relative_to(root)}: missing version marker {record['version']}")

        if all(path.exists() for path in paths.values()):
            canonical_invariants = extract_invariants(paths["canonical"])
            mirror_invariants = extract_invariants(paths["mirror"])
            if not canonical_invariants:
                issues.append(f"{record['canonical']}: no shared invariants declared")
            if canonical_invariants != mirror_invariants:
                issues.append(
                    f"{record['id']}: bilingual invariant mismatch "
                    f"{sorted(canonical_invariants)} != {sorted(mirror_invariants)}"
                )

    discovered_skill_files = {
        path.resolve()
        for path in [
            root / "SKILL.md",
            *root.glob("skills/*/SKILL.md"),
            *root.glob("skills-zh/*/SKILL.md"),
        ]
    }
    for path in sorted(discovered_skill_files - listed_skill_files):
        issues.append(f"skill is not listed in manifest: {path.relative_to(root)}")
    for path in sorted(listed_skill_files - discovered_skill_files):
        issues.append(f"manifest lists a non-skill path: {path.relative_to(root)}")

    for readme in (root / "README.md", root / "README_CN.md"):
        if not readme.exists():
            issues.append(f"missing {readme.name}")

    for path in root.rglob("*"):
        if ".git" in path.relative_to(root).parts:
            continue
        if path.is_file() and (
            path.name == ".env" or path.name.startswith(".env.")
            or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}
        ):
            issues.append(f"potential credential file should not be committed: {path.relative_to(root)}")

    for relative in sorted(REQUIRED_REPOSITORY_FILES):
        if not (root / relative).exists():
            issues.append(f"missing repository file: {relative}")

    templates = root / "assets/templates"
    for name in sorted(REQUIRED_TEMPLATES):
        if not (templates / name).exists():
            issues.append(f"missing template: assets/templates/{name}")

    eval_dir = root / "evals"
    for name in sorted(REQUIRED_EVALS):
        path = eval_dir / name
        if not path.exists():
            issues.append(f"missing eval: evals/{name}")
            continue
        kind = "trigger" if name.startswith("trigger") else "behavior"
        issues.extend(
            f"evals/{name}: {issue}"
            for issue in validate_eval(path, kind, seen_names)
        )
        if name == "forward-test-report.json":
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if payload.get("suite_version") != suite_version:
                issues.append(
                    "evals/forward-test-report.json: suite_version differs from manifest"
                )
            outcomes = [case.get("outcome") for case in payload.get("cases", [])]
            if not outcomes or any(outcome not in {"pass", "fail", "not_run"} for outcome in outcomes):
                issues.append(
                    "evals/forward-test-report.json: every case needs pass/fail/not_run outcome"
                )
            if "not_run" in outcomes and (
                payload.get("stage") != "pending_behavior_validation"
                or payload.get("release_ready") is not False
            ):
                issues.append("unrun behavior cases must explicitly block release readiness")
            for case in payload.get("cases", []):
                case_id = case.get("id", "unknown")
                if case.get("outcome") == "not_run":
                    if not case.get("reason"):
                        issues.append(f"{case_id}: unrun case requires a reason")
                    continue
                for field in ("language", "tested_skills", "evaluator", "review_trace"):
                    if not case.get(field):
                        issues.append(
                            f"evals/forward-test-report.json: {case_id} missing {field}"
                        )
                trace = case.get("review_trace")
                if isinstance(trace, str) and not (eval_dir / trace).exists():
                    issues.append(
                        f"evals/forward-test-report.json: {case_id} missing trace {trace}"
                    )

    issues.extend(check_evidence_counts(root))

    text_suffixes = {
        ".md", ".yaml", ".yml", ".json", ".py", ".toml", ".txt",
        ".tex", ".bib", ".csv", ".tsv", ".sh", ".ipynb",
    }
    active_text_files = [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix.lower() in text_suffixes
        and ".git" not in path.parts
    ]
    for path in active_text_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if PRIVATE_PATH_RE.search(text):
            issues.append(f"{path.relative_to(root)}: contains a private absolute path")
        if SECRET_RE.search(text):
            issues.append(f"{path.relative_to(root)}: contains a potential credential or private key")
        if path.name != "validate_suite.py" and (
            "Suite version: `2.0.0`" in text or "套件版本：`2.0.0`" in text
        ):
            issues.append(f"{path.relative_to(root)}: contains stale suite version")
        if path.suffix == ".md":
            issues.extend(f"{path.relative_to(root)}: {item}" for item in check_links(path))

    forbidden_artifact_suffixes = {
        ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".odt", ".rtf",
        ".tex", ".bib", ".csv", ".tsv", ".xls", ".xlsx", ".ods",
        ".zip", ".tar", ".gz", ".tgz", ".7z", ".rar",
        ".mat", ".h5", ".hdf5", ".npy", ".npz", ".pkl", ".pickle",
        ".joblib", ".pt", ".pth", ".ckpt", ".onnx", ".ipynb",
        ".parquet", ".feather", ".sqlite", ".db", ".sav", ".sas7bdat",
    }
    forbidden_artifacts = [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in forbidden_artifact_suffixes
    ]
    for path in forbidden_artifacts:
        issues.append(
            f"manuscript, archive, or data artifact should not be committed: {path.relative_to(root)}"
        )

    allowed_extensionless = {".gitignore", "LICENSE", "NOTICE", "Makefile"}
    for path in root.rglob("*"):
        if (
            path.is_file()
            and not path.suffix
            and path.name not in allowed_extensionless
            and ".git" not in path.parts
        ):
            issues.append(
                f"unreviewed extensionless file should not be committed: {path.relative_to(root)}"
            )

    for unwanted in (root / ".DS_Store", root / "local-corpus-map.yaml"):
        if unwanted.exists():
            issues.append(f"private/generated file should not be present: {unwanted.relative_to(root)}")

    return issues


def main() -> int:
    issues = validate(ROOT)
    if issues:
        print("Suite validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    _, records = parse_manifest(MANIFEST.read_text(encoding="utf-8"))
    print(f"Suite validation passed: {len(records)} bilingual skill pairs checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
