#!/usr/bin/env python3
"""Focused safety checks for source ZIP intake."""

from __future__ import annotations

import importlib.util
import stat
import tempfile
import unittest
import zipfile
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("safe_extract_zip.py")
SPEC = importlib.util.spec_from_file_location("safe_extract_zip", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class SafeExtractZipTests(unittest.TestCase):
    def make_zip(self, root: Path, entries: list[tuple[str, bytes, int | None]]) -> Path:
        path = root / "source.zip"
        with zipfile.ZipFile(path, "w") as archive:
            for name, data, mode in entries:
                info = zipfile.ZipInfo(name)
                if mode is not None:
                    info.create_system = 3
                    info.external_attr = mode << 16
                archive.writestr(info, data)
        return path

    def test_extracts_regular_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_zip(root, [("repo/SKILL.md", b"hello", stat.S_IFREG | 0o644)])
            module.extract(source, root / "out")
            self.assertEqual((root / "out/repo/SKILL.md").read_bytes(), b"hello")

    def test_rejects_traversal_and_windows_paths(self) -> None:
        for name in ("../escape", "/absolute", "repo\\escape", "C:/drive"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                source = self.make_zip(root, [(name, b"x", None)])
                with self.assertRaises(module.UnsafeArchive):
                    module.extract(source, root / "out")
                self.assertFalse((root / "escape").exists())

    def test_rejects_symlink_and_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_zip(root, [("link", b"target", stat.S_IFLNK | 0o777)])
            with self.assertRaises(module.UnsafeArchive):
                module.extract(source, root / "out")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_zip(root, [("A", b"1", None), ("a", b"2", None)])
            with self.assertRaises(module.UnsafeArchive):
                module.extract(source, root / "out")


if __name__ == "__main__":
    unittest.main()
