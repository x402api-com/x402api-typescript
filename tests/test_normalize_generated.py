from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


def _load_normalizer():
    path = Path(__file__).parents[1] / "scripts" / "normalize-generated.py"
    spec = importlib.util.spec_from_file_location("normalize_generated", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the generated-file normalizer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


normalizer = _load_normalizer()


class NormalizeGeneratedTests(unittest.TestCase):
    def test_selects_only_changed_top_level_tracked_file_keys(self) -> None:
        lock = """trackedFiles:
  src/index.ts:
    id: abc
  docs/example.md:
    id: def
features:
  typescript:
"""

        self.assertEqual(
            normalizer.changed_tracked_paths(
                lock,
                ["src/index.ts", "scripts/custom.py"],
            ),
            [Path("src/index.ts")],
        )

    def test_rejects_parent_traversal(self) -> None:
        lock = """trackedFiles:
  ../outside:
    id: abc
"""

        with self.assertRaisesRegex(ValueError, "unsafe generated path"):
            normalizer.tracked_paths(lock)

    def test_removes_trailing_whitespace_and_extra_blank_lines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "generated.ts"
            path.write_text("const answer = 42;  \n\n\n", encoding="utf-8")

            self.assertTrue(normalizer.normalize_file(path))
            self.assertEqual(path.read_text(encoding="utf-8"), "const answer = 42;\n")
            self.assertFalse(normalizer.normalize_file(path))

    def test_stages_only_the_explicit_normalized_paths(self) -> None:
        with mock.patch.object(normalizer.subprocess, "run") as run:
            normalizer.stage_paths([Path("src/index.ts"), Path("README.md")])

        run.assert_called_once_with(
            [
                "git",
                "-C",
                str(normalizer.ROOT),
                "add",
                "--update",
                "--",
                "src/index.ts",
                "README.md",
            ],
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
