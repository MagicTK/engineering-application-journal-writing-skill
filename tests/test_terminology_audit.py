import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("audit_terminology", ROOT / "scripts/audit_terminology.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TerminologyAuditTests(unittest.TestCase):
    def test_comments_are_not_manuscript(self):
        output = MODULE.audit("% variable-specific features\nprocess variables")
        self.assertFalse(output["candidates"])

    def test_escaped_percent(self):
        self.assertEqual(MODULE.strip_comment(r"90\% real data % offline"), r"90\% real data ")
        self.assertEqual(MODULE.strip_comment(r"row \\% comment"), r"row \\")

    def test_literal_branches_and_line_numbers(self):
        source = "\\iffalse\nrecords\n\\iftrue attributes\\fi\n\\else\noperating conditions\n\\fi"
        output = MODULE.audit(source)
        self.assertEqual([c["rule"] for c in output["candidates"]], ["state-condition"])
        self.assertEqual(output["candidates"][0]["occurrences"][0]["line"], 5)

    def test_comment_environment(self):
        output = MODULE.audit("\\begin{comment}\nrecords\n\\end{comment}\nprocess variables")
        self.assertFalse(output["candidates"])

    def test_bibliography_is_not_body_and_line_numbers_survive(self):
        source = "\n".join([
            "Process variables are measured.",
            r"\begin{thebibliography}{99}",
            r"\bibitem{old} Operating conditions and attributes.",
            r"\end{thebibliography}",
            "The local operational state guides prediction.",
        ])
        output = MODULE.audit(source, min_count=1, top=1000)
        self.assertEqual([c["rule"] for c in output["candidates"]], ["state-condition"])
        self.assertEqual(output["candidates"][0]["occurrences"][0]["line"], 5)
        self.assertFalse(any("attributes" in item["term"] for item in output["recurring_terms"]))
        self.assertIn("attributes", source)

    def test_reference_metadata_is_masked_but_link_prose_is_retained(self):
        source = "\n".join([
            r"\citep[see][p. 2]{records} \label{attributes} \url{https://example.org/offline}",
            r"\href{https://example.org/records}{operating conditions} remain relevant.",
        ])
        output = MODULE.audit(source)
        self.assertEqual([c["rule"] for c in output["candidates"]], ["state-condition"])
        self.assertEqual(output["candidates"][0]["occurrences"][0]["line"], 2)
        plain = MODULE.audit(r"\cite{attributes}", tex=False)
        self.assertEqual(plain["candidates"][0]["rule"], "attribute")

    def test_causal_convolution_is_a_context_question(self):
        output = MODULE.audit("A causal convolution uses past measurements.", tex=False)
        candidate = output["candidates"][0]
        self.assertEqual(candidate["rule"], "causality")
        self.assertIn("past-only", candidate["question"])
        self.assertNotIn("replacement", candidate)

    def test_candidates_are_not_bans(self):
        output = MODULE.audit("Semantic attributes and sensor records are legitimate.", tex=False)
        self.assertEqual(output["mode"], "review_candidates_only")
        self.assertEqual({c["rule"] for c in output["candidates"]}, {"attribute", "record"})
        self.assertTrue(all("replacement" not in item for item in output["candidates"]))

    def test_word_count_convention(self):
        output = MODULE.audit("\\begin{abstract}A compact dual-domain model.\\end{abstract}")
        self.assertEqual(output["abstract_whitespace_word_count"], 4)

    def test_no_global_substitution(self):
        source = "variable-specific behavior and variable-wise features"
        output = MODULE.audit(source, tex=False)
        self.assertEqual(output["candidates"][0]["count"], 2)
        self.assertIn("variable-specific", source)

    def test_repeated_phrases(self):
        output = MODULE.audit("Process variables. Process variables. Process variables.", tex=False)
        self.assertIn({"term": "process variables", "count": 3}, output["recurring_terms"])

    def test_membership_and_propagation_are_questions_not_replacements(self):
        output = MODULE.audit("Soft assignments guide message passing, not observed fault propagation.", tex=False)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(by_rule["membership-probability"]["count"], 1)
        self.assertEqual(by_rule["physical-propagation"]["count"], 2)
        self.assertTrue(all("replacement" not in item for item in by_rule.values()))

    def test_offline_assay_remains_a_context_question(self):
        output = MODULE.audit("Offline assay measurements supply delayed quality labels.", tex=False)
        candidate = output["candidates"][0]
        self.assertEqual(candidate["rule"], "offline")
        self.assertIn("measurement procedures", candidate["question"])
        self.assertNotIn("replacement", candidate)


if __name__ == "__main__":
    unittest.main()
