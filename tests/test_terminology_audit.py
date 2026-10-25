import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
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

    def test_inactive_comment_open_does_not_hide_active_branch(self):
        source = "\n".join([
            r"\iffalse", r"\begin{comment}", "attributes", r"\else",
            "operating conditions", r"\fi", "records",
        ])
        output = MODULE.audit(source)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(set(by_rule), {"state-condition", "record"})
        self.assertEqual(by_rule["state-condition"]["occurrences"][0]["line"], 5)
        self.assertEqual(by_rule["record"]["occurrences"][0]["line"], 7)

    def test_inactive_else_comment_open_does_not_hide_following_body(self):
        source = "\n".join([
            r"\iftrue", "operating conditions", r"\else",
            r"\begin{comment}", "attributes", r"\fi", "records",
        ])
        output = MODULE.audit(source)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(set(by_rule), {"state-condition", "record"})
        self.assertEqual(by_rule["record"]["occurrences"][0]["line"], 7)

    def test_inactive_comment_open_preserves_nested_conditional_depth(self):
        source = "\n".join([
            r"\iffalse", r"\begin{comment}", r"\iftrue", "attributes",
            r"\else", "offline", r"\fi", r"\else", "records", r"\fi",
        ])
        output = MODULE.audit(source)
        self.assertEqual([c["rule"] for c in output["candidates"]], ["record"])
        self.assertEqual(output["candidates"][0]["occurrences"][0]["line"], 9)

    def test_active_comment_body_does_not_change_literal_branch_state(self):
        source = "\n".join([
            r"\iftrue", r"\begin{comment}", r"\else", "attributes",
            r"\iffalse", r"\end{comment}", "operating conditions", r"\fi", "records",
        ])
        output = MODULE.audit(source)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(set(by_rule), {"state-condition", "record"})
        self.assertEqual(by_rule["state-condition"]["occurrences"][0]["line"], 7)

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

    def test_wrapped_candidates_keep_source_spans_and_frequency(self):
        source = "\n\n".join(["We use information\nexchange for learning."] * 3)
        source += "\n\nvariable-specific\nfeatures remain available."
        output = MODULE.audit(source, min_count=3, top=1000)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(by_rule.get("exchange", {}).get("count", 0), 3)
        occurrences = by_rule["exchange"]["occurrences"]
        self.assertEqual([(o["line"], o.get("end_line")) for o in occurrences], [(1, 2), (4, 5), (7, 8)])
        self.assertTrue(all(o["term"] == "information exchange" for o in occurrences))
        self.assertTrue(all("\n" not in o["context"] for o in occurrences))
        feature = by_rule["variable-feature"]["occurrences"][0]
        self.assertEqual((feature["line"], feature.get("end_line")), (10, 11))
        self.assertIn({"term": "information exchange", "count": 3}, output["recurring_terms"])

    def test_phrases_do_not_cross_paragraph_or_excluded_metadata_boundaries(self):
        sources = [
            "information\n\nexchange",
            "information\n  \nexchange",
            r"information\par exchange",
            "information\n\\begin{thebibliography}{9}\n\\bibitem{x} attributes\n\\end{thebibliography}\nexchange",
            r"information\begin{thebibliography}{9}\bibitem{x} attributes\end{thebibliography}exchange",
            r"information\label{not-a-space}exchange",
            r"information\cite{attributes}exchange",
            "information\n\\url{https://example.org/attributes}\nexchange",
        ]
        for source in sources:
            with self.subTest(source=source):
                output = MODULE.audit(source, min_count=1, top=1000)
                self.assertFalse(any(c["rule"] in {"exchange", "attribute"} for c in output["candidates"]))
                self.assertNotIn({"term": "information exchange", "count": 1}, output["recurring_terms"])

    def test_percent_newline_suppression_and_comment_only_lines(self):
        cases = [
            ("information% hidden attributes\nexchange", 0),
            ("information% hidden attributes\n  exchange", 0),
            ("information % hidden attributes\nexchange", 1),
            ("information\n% hidden attributes\nexchange", 1),
            ("information% hidden\n% hidden attributes\nexchange", 0),
            ("information% hidden\n% hidden attributes\n  exchange", 0),
        ]
        for source, expected in cases:
            with self.subTest(source=source):
                output = MODULE.audit(source, min_count=1, top=1000)
                by_rule = {item["rule"]: item for item in output["candidates"]}
                self.assertEqual(by_rule.get("exchange", {}).get("count", 0), expected)
                self.assertNotIn("attribute", by_rule)
                frequency = next((x["count"] for x in output["recurring_terms"] if x["term"] == "information exchange"), 0)
                self.assertEqual(frequency, expected)

    def test_wrapping_preserves_literal_branch_exclusion(self):
        source = "\n".join([
            r"\iffalse", "attributes", r"\else", "operating", "conditions remain relevant.", r"\fi",
            r"\begin{comment}", "records", r"\end{comment}",
        ])
        output = MODULE.audit(source)
        self.assertEqual([c["rule"] for c in output["candidates"]], ["state-condition"])
        occurrence = output["candidates"][0]["occurrences"][0]
        self.assertEqual((occurrence["line"], occurrence.get("end_line")), (4, 5))

    def test_plain_wrapping_does_not_enable_tex_comment_or_branch_rules(self):
        source = "information\nexchange\n% attributes\n\\iffalse records\\fi"
        output = MODULE.audit(source, tex=False)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(by_rule.get("exchange", {}).get("count", 0), 1)
        self.assertEqual(by_rule["attribute"]["count"], 1)
        self.assertEqual(by_rule["record"]["count"], 1)

    def test_cli_wrapped_audit_is_read_only(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.tex"
            source = "\n\n".join(["information\nexchange"] * 3).encode()
            path.write_bytes(source)
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / "scripts/audit_terminology.py"), str(path), "--min-count", "3"],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = json.loads(result.stdout)
            self.assertIn({"term": "information exchange", "count": 3}, output["recurring_terms"])
            self.assertEqual(path.read_bytes(), source)
            self.assertEqual(list(Path(folder).iterdir()), [path])

    def test_literal_space_rules_have_ordinary_wrapping_parity(self):
        phrases = [
            "operating conditions", "variable specific features", "variable-wise features",
            "cross stage", "stage level", "information exchange", "offline assay",
            "real time", "membership degrees", "message passing", "root cause", "development set",
        ]
        for phrase in phrases:
            words = phrase.split()
            flat = {item["rule"]: item["count"] for item in MODULE.audit(phrase)["candidates"]}
            for cut in range(1, len(words)):
                with self.subTest(phrase=phrase, cut=cut):
                    wrapped = " ".join(words[:cut]) + "\n" + " ".join(words[cut:])
                    actual = {item["rule"]: item["count"] for item in MODULE.audit(wrapped)["candidates"]}
                    self.assertEqual(actual, flat)

    def test_text_emphasis_preserves_phrase_candidates_and_frequency(self):
        source = "\n\n".join([
            r"We model operating \emph{conditions} and information \textbf{exchange}.",
        ] * 3)
        output = MODULE.audit(source, min_count=3, top=1000)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(by_rule.get("state-condition", {}).get("count", 0), 3)
        self.assertEqual(by_rule.get("exchange", {}).get("count", 0), 3)
        self.assertIn({"term": "operating conditions", "count": 3}, output["recurring_terms"])
        self.assertIn({"term": "information exchange", "count": 3}, output["recurring_terms"])

    def test_nested_text_emphasis_preserves_adjacency(self):
        source = r"\textbf{operating \emph{conditions}}. variable-\textit{specific} features. information\emph{exchange}."
        output = MODULE.audit(source, min_count=1, top=1000)
        by_rule = {item["rule"]: item for item in output["candidates"]}
        self.assertEqual(by_rule.get("state-condition", {}).get("count", 0), 1)
        self.assertEqual(by_rule.get("variable-feature", {}).get("count", 0), 1)
        self.assertNotIn("exchange", by_rule)
        self.assertIn({"term": "informationexchange", "count": 1}, output["recurring_terms"])

    def test_text_emphasis_keeps_comment_and_metadata_exclusions(self):
        source = "\n".join([
            r"% \emph{attributes} records",
            r"\iffalse \textbf{offline} \fi",
            r"information \emph{\cite{attributes}} exchange.",
            r"\textbf{operating \textit{conditions}} remain relevant.",
        ])
        output = MODULE.audit(source, min_count=1, top=1000)
        self.assertEqual([item["rule"] for item in output["candidates"]], ["state-condition"])
        self.assertEqual(output["candidates"][0]["occurrences"][0]["line"], 4)
        plain = MODULE.audit(r"information \emph{exchange}", tex=False)
        self.assertFalse(any(item["rule"] == "exchange" for item in plain["candidates"]))

    def test_multiline_text_emphasis_keeps_original_source_span(self):
        source = "information " + "\\textbf{\nexchange}."
        output = MODULE.audit(source, min_count=1, top=1000)
        exchange = next((item for item in output["candidates"] if item["rule"] == "exchange"), {})
        self.assertEqual(exchange.get("count", 0), 1)
        occurrence = exchange["occurrences"][0]
        self.assertEqual((occurrence["line"], occurrence["end_line"]), (1, 2))


if __name__ == "__main__":
    unittest.main()
