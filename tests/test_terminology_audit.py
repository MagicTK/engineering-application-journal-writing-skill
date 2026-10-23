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


if __name__ == "__main__":
    unittest.main()
