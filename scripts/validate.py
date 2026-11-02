#!/usr/bin/env python3
"""Validate required Atlas files, native agent metadata, and local Markdown links."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    ".claude/skills/roblox-research/SKILL.md",
    ".claude/agents/roblox-researcher.md",
    ".opencode/skills/roblox-research/SKILL.md",
    ".opencode/agents/roblox-researcher.md",
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
FRONTMATTER_FILES = {
    ".claude/skills/roblox-research/SKILL.md": {"description"},
    ".opencode/skills/roblox-research/SKILL.md": {"name", "description"},
    ".claude/agents/roblox-researcher.md": {"name", "description"},
    ".opencode/agents/roblox-researcher.md": {"description"},
}


def parse_frontmatter(text: str, relative: str) -> tuple[dict[str, str], str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, text, [f"missing YAML frontmatter: {relative}"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, text, [f"unterminated YAML frontmatter: {relative}"]

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")) and fields:
            continue
        match = re.fullmatch(r"([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*?)\s*", line)
        if not match:
            return fields, "\n".join(lines[end + 1 :]), [f"unsupported frontmatter line in {relative}: {line}"]
        fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return fields, "\n".join(lines[end + 1 :]), []


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    canonical_body: str | None = None
    canonical_path = root / "skills/roblox-research/SKILL.md"
    if canonical_path.is_file():
        canonical_text = canonical_path.read_text(encoding="utf-8")
        _, canonical_body, _ = parse_frontmatter(canonical_text, "skills/roblox-research/SKILL.md")

    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        if ".git" in path.parts or relative.startswith(".claude/worktrees/"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {relative}: {exc}")
            continue

        if relative in FRONTMATTER_FILES:
            fields, body, frontmatter_errors = parse_frontmatter(text, relative)
            errors.extend(frontmatter_errors)
            for key in FRONTMATTER_FILES[relative] - fields.keys():
                errors.append(f"missing {key} in frontmatter: {relative}")
            if relative.startswith(".opencode/skills/") and fields.get("name") != path.parent.name:
                errors.append(f"skill name must match directory in frontmatter: {relative}")
            if relative.endswith("/skills/roblox-research/SKILL.md") and canonical_body is not None and body != canonical_body:
                errors.append(f"skill instructions drift from canonical file: {relative}")

        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().split("#", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"link escapes repository in {relative}: {target}")
            elif not resolved.exists():
                errors.append(f"broken local link in {relative}: {target}")
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
    print("Atlas validation passed: required files, native metadata, skill parity, and local Markdown links are valid.")
    if args.self_check:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary)
            (fixture / "README.md").write_text("[missing](absent.md)\n", encoding="utf-8")
            fixture_errors = validate(fixture)
            assert f"missing required file: {REQUIRED_FILES[1]}" in fixture_errors
            assert "broken local link in README.md: absent.md" in fixture_errors
        print("Validator self-check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
