#!/usr/bin/env python3
"""Install the complete skill suite while preserving its shared directory layout."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = (
    Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    / "skills"
    / "engineering-application-journal-writing-skill"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the whole bilingual skill suite as one directory."
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help=f"final suite installation directory (default: {DEFAULT_TARGET})",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="copy the repository instead of creating a directory symlink",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the planned installation without changing the filesystem",
    )
    return parser.parse_args()


def copy_ignore(directory: str, names: list[str]) -> set[str]:
    ignored = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules", ".DS_Store"}
    if Path(directory).resolve() == ROOT:
        ignored.add("archive")
    return {name for name in names if name in ignored or name.endswith(".pyc")}


def main() -> int:
    args = parse_args()
    target = Path(os.path.abspath(args.target.expanduser()))
    mode = "copy" if args.copy else "symlink"

    resolved_target = target.resolve(strict=False)
    if resolved_target == ROOT or ROOT in resolved_target.parents:
        print("Refusing to install inside the source repository.", file=sys.stderr)
        return 2
    if target.exists() or target.is_symlink():
        print(
            f"Target already exists: {target}\n"
            "Remove or rename it explicitly after checking its contents; the installer will not overwrite it.",
            file=sys.stderr,
        )
        return 2

    print(f"Source: {ROOT}")
    print(f"Target: {target}")
    print(f"Mode:   {mode}")
    source_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_suite.py")], check=False
    )
    if source_check.returncode:
        print("Source validation failed; no installation was created.", file=sys.stderr)
        return source_check.returncode
    if args.dry_run:
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    if args.copy:
        shutil.copytree(ROOT, target, ignore=copy_ignore)
    else:
        target.symlink_to(ROOT, target_is_directory=True)

    validator = target / "scripts" / "validate_suite.py"
    result = subprocess.run([sys.executable, str(validator)], check=False)
    if result.returncode:
        print("Installation completed, but suite validation failed.", file=sys.stderr)
        return result.returncode

    print("Installation validated. Restart or refresh the client to discover the skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
