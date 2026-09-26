#!/usr/bin/env python3
"""Validate the structural contract for .project-ai lifecycle skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED_HEADINGS = [
    "Purpose",
    "Workflow",
    "Output contract",
    "Boundaries",
    "Completion gate",
]
BANNED_RUNTIME_MARKERS = [
    "## Provenance",
    "_bmad/",
    ".sdlc/",
    "docs/superpowers/",
    ".superpowers/",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---
"):
        raise ValueError("frontmatter must start on line 1")
    end = text.find("
---
", 4)
    if end == -1:
        raise ValueError("frontmatter closing delimiter not found")
    raw = text[4:end]
    body = text[end + 5 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, body


def heading_positions(body: str) -> dict[str, int]:
    positions: dict[str, int] = {}
    for match in re.finditer(r"^##\s+(.+?)\s*$", body, re.MULTILINE):
        positions[match.group(1)] = match.start()
    return positions


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    line_count = len(text.splitlines())

    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]

    name = fields.get("name", "")
    description = fields.get("description", "")

    if name != skill_dir.name:
        errors.append(
            f"{skill_dir.name}: frontmatter name {name!r} does not match directory"
        )
    if not description.startswith("Use when "):
        errors.append(f"{skill_dir.name}: description must start with 'Use when '")
    if len(description) > 500:
        errors.append(
            f"{skill_dir.name}: description is {len(description)} chars; keep <= 500"
        )
    if line_count > 500:
        errors.append(f"{skill_dir.name}: SKILL.md is {line_count} lines; keep <= 500")

    headings = heading_positions(body)
    last = -1
    for heading in REQUIRED_HEADINGS:
        if heading not in headings:
            errors.append(f"{skill_dir.name}: missing required heading '## {heading}'")
            continue
        if headings[heading] <= last:
            errors.append(
                f"{skill_dir.name}: required headings are not in canonical order"
            )
        last = headings[heading]

    for marker in BANNED_RUNTIME_MARKERS:
        if marker in text:
            errors.append(
                f"{skill_dir.name}: runtime file contains maintenance/upstream marker {marker!r}"
            )

    return errors


def main() -> int:
    skill_dirs = sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )

    errors: list[str] = []
    names: set[str] = set()

    for skill_dir in skill_dirs:
        skill_errors = validate_skill(skill_dir)
        errors.extend(skill_errors)

        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            try:
                fields, _ = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
                name = fields.get("name", "")
                if name in names:
                    errors.append(f"{skill_dir.name}: duplicate skill name {name!r}")
                names.add(name)
            except ValueError:
                pass

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed: {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
