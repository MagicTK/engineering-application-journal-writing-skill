#!/usr/bin/env python3
"""Create a new clean export; never publish or include the parent repository."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

from validate_suite import validate

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".DS_Store", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
ROOT_FILES = {"README.md", "README_CN.md", "SKILL.md", "suite-manifest.yaml", "LICENSE", "NOTICE", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md", ".gitignore"}
ROOT_DIRS = {".github", "agents", "assets", "evals", "references", "scripts", "skills", "skills-zh", "tests", "tools"}


def behavior_source_hashes(root: Path) -> dict[str, str]:
    """Identify the executable instructions and dependencies actually evaluated."""
    paths = [root / "SKILL.md", root / "suite-manifest.yaml"]
    for folder in ("skills", "skills-zh", "references", "assets", "scripts", "tools"):
        paths.extend((root / folder).rglob("*"))
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(paths)
        if path.is_file() and not path.is_symlink()
        and not any(part in IGNORED for part in path.relative_to(root).parts)
        and path.suffix != ".pyc"
    }


def release_issues(root: Path) -> list[str]:
    issues = []
    if not (root / "LICENSE").is_file():
        issues.append("distribution license not finalized")
    report = json.loads((root / "evals/forward-test-report.json").read_text())
    if report.get("release_ready") is not True:
        issues.append("behavioral release readiness not confirmed")
    if not report.get("independent_fresh_contexts"):
        issues.append("independent behavioral test not recorded")
    if not report.get("cases") or any(c.get("outcome") != "pass" for c in report["cases"]):
        issues.append("behavioral cases contain failures or unrun cases")
    hashes = report.get("evaluated_source_sha256")
    if not isinstance(hashes, dict) or not hashes:
        issues.append("evaluated instruction/source fingerprints not recorded")
    elif hashes != behavior_source_hashes(root):
        issues.append("instructions or dependencies differ from the behavior-tested snapshot")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--draft", action="store_true", help="Allow a local draft export with pending publication gates")
    args = parser.parse_args()
    destination = args.destination.expanduser().absolute()
    resolved = destination.resolve()
    if destination.exists() or destination.is_symlink():
        parser.error("destination already exists; no files were overwritten")
    if resolved == ROOT or ROOT in resolved.parents or resolved in ROOT.parents:
        parser.error("destination must be outside the source and its ancestors")
    issues = validate(ROOT)
    if not args.draft:
        issues += release_issues(ROOT)
    if issues:
        print("Export blocked:\n" + "\n".join(issues), file=sys.stderr)
        return 1
    selected = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in IGNORED for part in relative.parts) or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            parser.error(f"review symlink before export: {relative}")
        if not path.is_file():
            continue
        if len(relative.parts) == 1 and path.name not in ROOT_FILES:
            parser.error(f"unreviewed root file: {relative}")
        if len(relative.parts) > 1 and relative.parts[0] not in ROOT_DIRS:
            parser.error(f"unreviewed root directory: {relative.parts[0]}")
        selected.append((path, relative))
    destination.mkdir(parents=True)
    for path, relative in selected:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    issues = validate(destination)
    if issues:
        print("Export created but verification failed:\n"+"\n".join(issues), file=sys.stderr)
        return 1
    print(f"Exported and structurally checked {len(selected)} files: {destination}")
    print("Local draft only; publication gates may remain." if args.draft else "Release export ready; nothing has been published.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
