import runpy
import unittest
from pathlib import Path


demo = runpy.run_path(str(Path(__file__).resolve().parents[1] / "assets/examples/request-accounting.py"))


class RequestAccountingTests(unittest.TestCase):
    def test_fixture_and_inclusive_deadline(self):
        result = demo["counts"](demo["REQUESTS"], 100)
        self.assertEqual(list(result.values()), [(3, 4), (4, 6), (2, 6)])
        self.assertEqual(demo["counts"](demo["REQUESTS"], 99)["timely correct delivery"], (1, 6))

    def test_handoffs_do_not_disappear_or_become_diagnostic_answers(self):
        self.assertEqual(list(demo["counts"]([demo["REQUESTS"][-1]], 100).values()),
                         [(0, 0), (0, 1), (0, 1)])

    def test_retries_and_missing_references_are_not_incorrect_answers(self):
        with self.assertRaises(ValueError):
            demo["counts"]([demo["REQUESTS"][0]] * 2, 100)
        with self.assertRaises(ValueError):
            demo["counts"]([demo["Request"]("X", "answer", None, 18, 1)], 100)
