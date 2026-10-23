import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
SPEC = importlib.util.spec_from_file_location('export_public', ROOT / 'scripts/export_public.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReleaseGateTests(unittest.TestCase):
    def test_installer_preserves_dangling_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root/'existing-link'
            missing = root/'missing-location'
            target.symlink_to(missing, target_is_directory=True)
            result = subprocess.run([sys.executable, str(ROOT/'scripts/install_suite.py'), '--copy', '--target', str(target)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertTrue(target.is_symlink())
            self.assertFalse(missing.exists())

    def test_pending_cannot_be_published(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'evals').mkdir()
            (root/'evals/forward-test-report.json').write_text(json.dumps({'release_ready':False,'independent_fresh_contexts':False,'cases':[{'outcome':'not_run'}]}))
            issues = MODULE.release_issues(root)
            self.assertEqual(len(issues), 5)

    def test_completed_gate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'evals').mkdir()
            (root/'LICENSE').write_text('Synthetic test fixture, not a license grant.')
            (root/'SKILL.md').write_text('Synthetic instructions')
            report = {'release_ready':True,'independent_fresh_contexts':True,'cases':[{'outcome':'pass'}], 'evaluated_source_sha256':MODULE.behavior_source_hashes(root)}
            (root/'evals/forward-test-report.json').write_text(json.dumps(report))
            self.assertEqual(MODULE.release_issues(root), [])
            (root/'SKILL.md').write_text('Changed after evaluation')
            self.assertIn('instructions or dependencies differ from the behavior-tested snapshot', MODULE.release_issues(root))

    def test_added_dependency_invalidates_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'SKILL.md').write_text('Synthetic instructions')
            before = MODULE.behavior_source_hashes(root)
            (root/'references').mkdir()
            (root/'references/new.md').write_text('New behavior instructions')
            self.assertNotEqual(before, MODULE.behavior_source_hashes(root))


if __name__ == '__main__':
    unittest.main()
