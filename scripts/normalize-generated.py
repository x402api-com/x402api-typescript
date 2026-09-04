#!/usr/bin/env python3
"""Normalize whitespace only in generated files changed by this release."""

from __future__ import annotations

import argparse
import subprocess
from collections.abc import Iterable
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / ".speakeasy" / "gen.lock"


def _safe_relative(raw_path: str) -> PurePosixPath:
    relative = PurePosixPath(raw_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"unsafe generated path: {raw_path}")
    return relative


def tracked_paths(lock_text: str) -> set[PurePosixPath]:
    paths: set[PurePosixPath] = set()
    in_tracked_files = False
    for line in lock_text.splitlines():
        if line == "trackedFiles:":
            in_tracked_files = True
            continue
        if in_tracked_files and line and not line.startswith(" "):
            break
        if not in_tracked_files or not line.startswith("  "):
            continue
        if line.startswith("    ") or not line.endswith(":"):
            continue
        paths.add(_safe_relative(line[2:-1]))
    if not paths:
        raise ValueError("Speakeasy lock contains no tracked files")
    return paths


def changed_tracked_paths(
    lock_text: str,
    changed_paths: Iterable[str],
) -> list[PurePosixPath]:
    tracked = tracked_paths(lock_text)
    changed = {_safe_relative(path) for path in changed_paths if path}
    return sorted(tracked & changed, key=str)


def _git_paths(*args: str) -> set[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args, "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return {path for path in result.stdout.decode("utf-8").split("\0") if path}


def release_changed_paths(base_ref: str = "origin/main") -> set[str]:
    return set().union(
        _git_paths("diff", "--name-only", "--diff-filter=ACMRT", f"{base_ref}...HEAD"),
        _git_paths("diff", "--name-only", "--diff-filter=ACMRT"),
        _git_paths("diff", "--cached", "--name-only", "--diff-filter=ACMRT"),
        _git_paths("ls-files", "--others", "--exclude-standard"),
    )


def normalize_file(path: Path) -> bool:
    if not path.is_file() or path.is_symlink():
        return False
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    lines = original.splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    normalized = "\n".join(line.rstrip(" \t") for line in lines)
    if normalized:
        normalized += "\n"
    if normalized == original:
        return False
    path.write_text(normalized, encoding="utf-8")
    return True


def stage_paths(paths: Iterable[PurePosixPath]) -> None:
    selected = [str(path) for path in paths]
    if not selected:
        return
    subprocess.run(
        ["git", "-C", str(ROOT), "add", "--update", "--", *selected],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage",
        action="store_true",
        help="stage only files whose whitespace was normalized",
    )
    args = parser.parse_args()
    lock_text = LOCK.read_text(encoding="utf-8")
    normalized: list[PurePosixPath] = []
    for relative in changed_tracked_paths(lock_text, release_changed_paths()):
        if normalize_file(ROOT.joinpath(*relative.parts)):
            normalized.append(relative)
    if args.stage:
        stage_paths(normalized)


if __name__ == "__main__":
    main()
