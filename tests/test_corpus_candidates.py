import importlib.util
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("corpus_candidates", ROOT / "tools/extract_terminology_evidence.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CorpusCandidateTests(unittest.TestCase):
    def test_page_and_candidate_state(self):
        result = MODULE.scan_pages(["Introduction", "A gating mechanism weights features."], "gating mechanism", 3, 80)
        self.assertEqual(result["contexts"][0]["pdf_page"], 2)
        self.assertEqual(result["contexts"][0]["status"], "candidate_not_semantically_verified")
        self.assertFalse(result["reference_heading_detected"])

    def test_reference_regions_are_not_body_evidence(self):
        result = MODULE.scan_pages(["Feature fusion combines paths.\nR EFERENCES\n[1] Feature fusion.", "Feature fusion."], "feature fusion", 4, 80)
        self.assertEqual(result["region_counts"], {"unverified_body": 1, "references_or_later": 2})
        self.assertTrue(result["reference_heading_detected"])

    def test_reference_word_inside_sentence_is_not_heading(self):
        result = MODULE.scan_pages(["This references feature fusion."], "feature fusion", 3, 80)
        self.assertFalse(result["reference_heading_detected"])

    def test_qualifiers_do_not_create_semantic_equivalence(self):
        result = MODULE.scan_pages(["A gating mechanism."], "age-aware gating", 3, 80)
        self.assertEqual(result["candidate_occurrences"], 0)

    def test_hyphen_and_space_variation_only(self):
        result = MODULE.scan_pages(["Self-\nattention and self attention. Not cross-attention."], "self-attention", 3, 80)
        self.assertEqual(result["candidate_occurrences"], 2)

    def test_same_name_is_not_same_content(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/"a", Path(directory)/"b"
            a.mkdir()
            b.mkdir()
            first, second = a/"paper.pdf", b/"paper.pdf"
            first.write_bytes(b"first fictional content")
            second.write_bytes(b"second fictional content")
            self.assertNotEqual(MODULE.file_sha256(first), MODULE.file_sha256(second))
            second.write_bytes(first.read_bytes())
            self.assertEqual(MODULE.file_sha256(first), MODULE.file_sha256(second))

    def test_cli_retains_different_same_name_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            a, b = root/"a", root/"b"
            a.mkdir()
            b.mkdir()
            (a/"paper.pdf").write_bytes(b"fictional first work")
            (b/"paper.pdf").write_bytes(b"fictional second work")
            (b/"copy.pdf").write_bytes(b"fictional first work")
            terms, output = root/"terms.txt", root/"candidates.json"
            terms.write_text("feature fusion\n")
            argv = ["search", "--corpus", f"a={a}", "--corpus", f"b={b}",
                    "--terms", str(terms), "--output", str(output)]
            with patch("sys.argv", argv), patch.object(MODULE, "pdf_pages", return_value=["Feature fusion."]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(MODULE.main(), 0)
            result = json.loads(output.read_text())
            self.assertEqual(result["unique_file_count"], 2)
            self.assertEqual(len(result["byte_identical_files_skipped"]), 1)
            self.assertEqual(len(result["same_name_files_retained"]["paper"]), 2)
            self.assertEqual(result["status"], "candidate_search_only")
            self.assertNotIn("paper_count", result)

    def test_missing_pdf_dependency_fails_without_replacing_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/"paper.pdf").write_bytes(b"fictional PDF fixture")
            terms, output = root/"terms.txt", root/"report.json"
            terms.write_text("feature fusion\n")
            output.write_text('{"existing": true}\n')
            argv = ["search", "--corpus", f"fictional={root}", "--terms", str(terms), "--output", str(output)]
            error = ModuleNotFoundError("No module named 'pypdf'", name="pypdf")
            stderr = io.StringIO()
            with patch("sys.argv", argv), patch.object(MODULE, "pdf_pages", side_effect=error), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                self.assertEqual(MODULE.main(), 2)
            self.assertIn("pypdf", stderr.getvalue())
            self.assertEqual(output.read_text(), '{"existing": true}\n')

    def test_partial_pdf_failure_preserves_candidates_but_signals_incomplete(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/"good.pdf").write_bytes(b"fictional readable PDF")
            (root/"broken.pdf").write_bytes(b"fictional broken PDF")
            terms, output = root/"terms.txt", root/"report.json"
            terms.write_text("feature fusion\n")
            argv = ["search", "--corpus", f"fictional={root}", "--terms", str(terms), "--output", str(output)]
            def reader(path):
                if path.name == "broken.pdf":
                    raise ValueError("unreadable fixture")
                return ["Feature fusion combines inputs."]
            with patch("sys.argv", argv), patch.object(MODULE, "pdf_pages", side_effect=reader), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(MODULE.main(), 1)
            result = json.loads(output.read_text())
            self.assertEqual(result["coverage"]["status"], "partial")
            self.assertEqual(result["coverage"]["searchable_unique_files"], 1)
            self.assertEqual(result["coverage"]["failed_file_reads"], 1)
            self.assertEqual(len(result["evidence"]["feature fusion"]), 1)
            self.assertEqual(result["status"], "candidate_search_only")

    def test_all_pdf_reads_failed_are_not_successful_zero_hits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/"broken.pdf").write_bytes(b"fictional broken PDF")
            terms, output = root/"terms.txt", root/"report.json"
            terms.write_text("feature fusion\n")
            argv = ["search", "--corpus", f"fictional={root}", "--terms", str(terms), "--output", str(output)]
            with patch("sys.argv", argv), patch.object(MODULE, "pdf_pages", side_effect=ValueError("broken")), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(MODULE.main(), 1)
            result = json.loads(output.read_text())
            self.assertEqual(result["coverage"]["status"], "failed")
            self.assertEqual(result["coverage"]["parsed_unique_files"], 0)
            self.assertEqual(len(result["failures"]), 1)

    def test_textless_pdf_is_retained_but_not_counted_as_searchable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/"blank.pdf").write_bytes(b"fictional no-text PDF")
            terms, output = root/"terms.txt", root/"report.json"
            terms.write_text("feature fusion\n")
            argv = ["search", "--corpus", f"fictional={root}", "--terms", str(terms), "--output", str(output)]
            with patch("sys.argv", argv), patch.object(MODULE, "pdf_pages", return_value=["", "  "]), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(MODULE.main(), 1)
            result = json.loads(output.read_text())
            self.assertEqual(result["unique_file_count"], 1)
            self.assertEqual(result["coverage"]["status"], "failed")
            self.assertEqual(result["coverage"]["searchable_unique_files"], 0)
            self.assertEqual(result["coverage"]["unsearchable_unique_files"], 1)
            self.assertEqual(result["files"][0]["text_pages"], 0)
            self.assertEqual(result["evidence"], {})

    def test_empty_corpus_is_explicit_not_negative_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            terms, output = root/"terms.txt", root/"report.json"
            terms.write_text("feature fusion\n")
            argv = ["search", "--corpus", f"fictional={root}", "--terms", str(terms), "--output", str(output)]
            with patch("sys.argv", argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(MODULE.main(), 0)
            result = json.loads(output.read_text())
            self.assertEqual(result["coverage"]["status"], "empty")
            self.assertEqual(result["coverage"]["searchable_unique_files"], 0)


if __name__ == "__main__":
    unittest.main()
