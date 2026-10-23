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


if __name__ == "__main__":
    unittest.main()
