from copy import deepcopy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


EXAMPLE = Path(__file__).resolve().parents[1] / "assets/examples/result-workflow"
SPEC = importlib.util.spec_from_file_location("result_demo", EXAMPLE / "build.py")
DEMO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DEMO)


class ResultWorkflowExampleTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads((EXAMPLE / "fixture.json").read_text())

    def test_exact_single_table_metrics(self):
        result = DEMO.metrics([[76, 4], [8, 12]])
        self.assertEqual(result["accuracy"], Fraction(88, 100))
        expected = (Fraction(152, 164) + Fraction(24, 36)) / 2
        self.assertEqual(result["macro_f1"], expected)
        self.assertEqual(result["weighted_f1"],
                         (80 * Fraction(152, 164) + 20 * Fraction(24, 36)) / 100)

    def test_summary_and_saved_table(self):
        result = DEMO.summarize(self.fixture)
        expected = {
            "Reference A": (0.7990481884741767, 0.0075067731939615625),
            "Variant B": (0.8272965888634023, 0.023341040680824474),
        }
        for method, (average, sd) in expected.items():
            summary = result[method]["summary"]["macro_f1"]
            self.assertAlmostEqual(summary["mean"], average)
            self.assertAlmostEqual(summary["sample_sd"], sd)
        self.assertLess(result["Variant B"]["table_metrics"][1]["macro_f1"],
                        result["Reference A"]["table_metrics"][1]["macro_f1"])
        self.assertEqual(DEMO.markdown_table(result),
                         (EXAMPLE / "table.md").read_text())

    def test_missing_and_duplicate_tables_rejected(self):
        for mode in ("missing", "duplicate_id", "duplicate_repetition"):
            value = deepcopy(self.fixture)
            if mode == "missing":
                value["runs"].pop()
            elif mode == "duplicate_id":
                value["runs"][1]["run_id"] = value["runs"][0]["run_id"]
            else:
                value["runs"][1]["repetition"] = 1
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                DEMO.summarize(value)

    def test_invalid_counts_rejected(self):
        for matrix in ([[0, 0], [0, 0]], [[-1, 1], [2, 3]],
                       [[1.5, 0], [0, 2]], [[True, 0], [0, 2]], [[1, 2]]):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                DEMO.metrics(matrix)

    def test_metadata_mismatch_rejected(self):
        for key, replacement in (("fictional", False), ("matrix_rows", "predictions"),
                                 ("class_support", [79, 21]),
                                 ("unique_test_examples", 300),
                                 ("methods", ["Reference A"]),
                                 ("expected_repetitions_per_method", 1)):
            value = deepcopy(self.fixture)
            value[key] = replacement
            with self.subTest(key=key), self.assertRaises(ValueError):
                DEMO.summarize(value)

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "keep.txt"
            marker.write_text("existing result")
            process = subprocess.run([sys.executable, "-B", str(EXAMPLE / "build.py"),
                                      "--output", directory], capture_output=True, text=True)
            self.assertEqual(process.returncode, 2)
            self.assertIn("already exists", process.stderr)
            self.assertEqual(marker.read_text(), "existing result")
            self.assertEqual(list(Path(directory).iterdir()), [marker])


if __name__ == "__main__":
    unittest.main()
