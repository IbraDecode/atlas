#!/usr/bin/env python3
"""Validate required Atlas files and local Markdown links using only stdlib."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "core/engineering-standards.md",
    "core/security-policy.md",
    "skills/roblox-research/SKILL.md",
    "agents/roblox-researcher.md",
    "adapters/claude-code/README.md",
    "adapters/opencode/README.md",
    "integrations/roblox-studio/README.md",
    "integrations/research/README.md",
    "docs/architecture.md",
    "docs/contributing.md",
    "docs/references.md",
    "docs/roadmap.md",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {path.relative_to(root)}: {exc}")
            continue
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().split("#", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"link escapes repository in {path.relative_to(root)}: {target}")
            elif not resolved.exists():
                errors.append(f"broken local link in {path.relative_to(root)}: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true", help="run a temporary fixture self-check")
    args = parser.parse_args()
    errors = validate()
    if errors:
        print("Atlas validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Atlas validation passed: required files and local Markdown links are valid.")
    if args.self_check:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary)
            (fixture / "README.md").write_text("[missing](absent.md)\\n", encoding="utf-8")
            fixture_errors = validate(fixture)
            assert f"missing required file: {REQUIRED_FILES[1]}" in fixture_errors
            assert "broken local link in README.md: absent.md" in fixture_errors
        print("Validator self-check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
