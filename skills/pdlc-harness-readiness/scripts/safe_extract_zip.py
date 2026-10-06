#!/usr/bin/env python3
"""Extract a source ZIP without allowing traversal, links, or oversized payloads."""

from __future__ import annotations

import argparse
import shutil
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath

MAX_MEMBERS = 20_000
MAX_FILE_BYTES = 100 * 1024 * 1024
MAX_TOTAL_BYTES = 1024 * 1024 * 1024


class UnsafeArchive(ValueError):
    pass


def checked_members(archive: zipfile.ZipFile) -> list[tuple[zipfile.ZipInfo, PurePosixPath]]:
    members: list[tuple[zipfile.ZipInfo, PurePosixPath]] = []
    seen: set[str] = set()
    total = 0
    infos = archive.infolist()
    if len(infos) > MAX_MEMBERS:
        raise UnsafeArchive("too many archive entries")
    for info in infos:
        name = info.filename
        if not name or "\\" in name or name.startswith("/") or "\x00" in name:
            raise UnsafeArchive("invalid archive path")
        path = PurePosixPath(name)
        if any(part in ("", ".", "..") for part in path.parts) or ":" in path.parts[0]:
            raise UnsafeArchive("archive path escapes destination")
        key = str(path).casefold()
        if key in seen:
            raise UnsafeArchive("duplicate archive path")
        seen.add(key)
        if info.flag_bits & 0x1:
            raise UnsafeArchive("encrypted archive entry")
        kind = stat.S_IFMT(info.external_attr >> 16)
        if kind not in (0, stat.S_IFREG, stat.S_IFDIR):
            raise UnsafeArchive("links or special files are not supported")
        if info.file_size > MAX_FILE_BYTES:
            raise UnsafeArchive("archive entry exceeds size limit")
        total += info.file_size
        if total > MAX_TOTAL_BYTES:
            raise UnsafeArchive("archive exceeds total size limit")
        members.append((info, path))
    return members


def extract(zip_path: Path, destination: Path) -> None:
    if destination.exists() and any(destination.iterdir()):
        raise UnsafeArchive("destination must be empty")
    with zipfile.ZipFile(zip_path) as archive:
        members = checked_members(archive)
        destination.mkdir(parents=True, exist_ok=True)
        root = destination.resolve()
        for info, path in members:
            target = destination.joinpath(*path.parts)
            if not target.resolve().is_relative_to(root):
                raise UnsafeArchive("archive path escapes destination")
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, target.open("xb") as output:
                shutil.copyfileobj(source, output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        extract(args.zip_path, args.destination)
    except (OSError, zipfile.BadZipFile, RuntimeError, UnsafeArchive) as exc:
        print(f"Unsafe or unreadable ZIP: {exc}", file=sys.stderr)
        return 2
    print(f"Extracted source snapshot to {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
