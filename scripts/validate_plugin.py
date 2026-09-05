#!/usr/bin/env python3
"""Keep this repo installable.

Four manifests describe one plugin to two hosts. They agree the day they are
written and diverge the first time someone edits one by hand, and nothing else
in a repo notices — the plugin just installs wrong, or empty, for whoever picked
the host you did not test.

Also checks the layout the manifests promise: Claude and Codex both resolve
skills as `skills/<name>/SKILL.md`, so a skill that drifts back to a flat file,
or whose frontmatter name stops matching its directory, silently stops being
found.

Usage: python3 scripts/validate_plugin.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

CLAUDE_MARKET = ROOT / ".claude-plugin" / "marketplace.json"
CLAUDE_PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
CODEX_MARKET = ROOT / ".agents" / "plugins" / "marketplace.json"
CODEX_PLUGIN = ROOT / ".codex-plugin" / "plugin.json"

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def frontmatter(text: str) -> dict[str, str] | None:
    """Minimal top-level scalar parse — enough for name/description, no PyYAML."""
    match = FRONTMATTER.match(text)
    if not match:
        return None
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if re.match(r"^[A-Za-z][\w-]*:", line):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip().strip("\"'")
    return out


def main() -> int:
    errors: list[str] = []

    manifests = {}
    for label, path in (
        ("claude marketplace", CLAUDE_MARKET),
        ("claude plugin", CLAUDE_PLUGIN),
        ("codex marketplace", CODEX_MARKET),
        ("codex plugin", CODEX_PLUGIN),
    ):
        try:
            manifests[label] = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            errors.append(f"missing manifest: {path.relative_to(ROOT)}")
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")

    if len(manifests) == 4:
        cm, cp = manifests["claude marketplace"], manifests["claude plugin"]
        xm, xp = manifests["codex marketplace"], manifests["codex plugin"]
        entry, xentry = cm["plugins"][0], xm["plugins"][0]

        for field, a, b in (
            ("plugin name", cp["name"], xp["name"]),
            ("plugin version", cp["version"], xp["version"]),
            ("plugin description", cp["description"], xp["description"]),
            ("marketplace name", cm["name"], xm["name"]),
            ("listed plugin name", entry["name"], xentry["name"]),
            ("listed version", entry["version"], xentry["version"]),
            ("listed description", entry["description"], xentry["description"]),
        ):
            if a != b:
                errors.append(f"Claude and Codex manifests disagree on {field}")

        # Within a host, the marketplace entry and the plugin must also agree.
        for field, a, b in (
            ("name", cp["name"], entry["name"]),
            ("version", cp["version"], entry["version"]),
            ("description", cp["description"], entry["description"]),
        ):
            if a != b:
                errors.append(
                    f"Claude's marketplace entry and plugin.json disagree on {field}"
                )

        # Codex resolves skills from this path. Wrong or missing, and the plugin
        # installs with nothing in it — no error, just an empty install.
        if xp.get("skills") != "./skills/":
            errors.append('.codex-plugin/plugin.json must set "skills" to "./skills/"')
        if not xp.get("interface", {}).get("displayName"):
            errors.append(".codex-plugin/plugin.json is missing interface.displayName")
        if not xp.get("interface", {}).get("shortDescription"):
            errors.append(".codex-plugin/plugin.json is missing interface.shortDescription")
        if not xm.get("interface", {}).get("displayName"):
            errors.append(".agents/plugins/marketplace.json is missing interface.displayName")
        # Codex takes a structured source; Claude takes a string. Copying one
        # across is the easiest way to break exactly one host.
        if not isinstance(xentry.get("source"), dict):
            errors.append(".agents/plugins/marketplace.json source must be an object")
        if not isinstance(entry.get("source"), str):
            errors.append(".claude-plugin/marketplace.json source must be a string")
        if not xentry.get("policy", {}).get("installation"):
            errors.append(".agents/plugins/marketplace.json entry is missing policy.installation")

    # The layout both hosts resolve against.
    if not SKILLS.is_dir():
        errors.append("no skills/ directory")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
        for stray in sorted(SKILLS.glob("*.md")):
            errors.append(
                f"skills/{stray.name} is a flat file — skills must be "
                f"skills/{stray.stem}/SKILL.md or neither host will find it"
            )

    for directory in skill_dirs:
        skill_md = directory / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"skills/{directory.name}/ has no SKILL.md")
            continue
        front = frontmatter(skill_md.read_text(encoding="utf-8"))
        if front is None:
            errors.append(f"skills/{directory.name}/SKILL.md has no frontmatter")
            continue
        if front.get("name") != directory.name:
            errors.append(
                f"skills/{directory.name}/SKILL.md declares name "
                f"{front.get('name')!r}, which is not its directory name"
            )
        if not front.get("description"):
            errors.append(f"skills/{directory.name}/SKILL.md has no description")

    # Every skills/... path this repo points at has to resolve, or the reader is
    # sent to a file that moved.
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for ref in re.findall(r"skills/[A-Za-z0-9._/-]+", md.read_text(encoding="utf-8", errors="replace")):
            target = ref.rstrip(".,;:)`\"'")
            if target.endswith("/"):
                continue
            if not (ROOT / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: dead path -> {target}")

    if errors:
        print(f"FAIL — {len(errors)} problem(s):\n", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(f"OK — {len(skill_dirs)} skills, four manifests in agreement")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
