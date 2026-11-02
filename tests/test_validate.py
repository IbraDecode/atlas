import tempfile
import unittest
from pathlib import Path

from scripts.validate import REQUIRED_FILES, parse_frontmatter, validate


class ValidateTests(unittest.TestCase):
    def test_frontmatter_required_fields_and_directory_name(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for relative in REQUIRED_FILES:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# fixture\n", encoding="utf-8")
            canonical = root / "skills/roblox-research/SKILL.md"
            canonical.write_text("---\nname: roblox-research\ndescription: Test\n---\n\nBody.\n", encoding="utf-8")
            opencode_skill = root / ".opencode/skills/roblox-research/SKILL.md"
            opencode_skill.write_text("---\nname: other-name\ndescription: Test\n---\n\nDifferent.\n", encoding="utf-8")
            errors = validate(root)
            self.assertIn("skill name must match directory in frontmatter: .opencode/skills/roblox-research/SKILL.md", errors)
            self.assertIn("skill instructions drift from canonical file: .opencode/skills/roblox-research/SKILL.md", errors)

    def test_parse_frontmatter_requires_closing_delimiter(self):
        fields, _, errors = parse_frontmatter("---\nname: sample\n", "sample.md")
        self.assertEqual(fields, {})
        self.assertEqual(errors, ["unterminated YAML frontmatter: sample.md"])

    def test_repository_passes(self):
        self.assertEqual(validate(Path(__file__).resolve().parents[1]), [])

    def test_reports_missing_required_file_and_broken_link(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("[missing](absent.md)\n", encoding="utf-8")

            errors = validate(root)

            self.assertIn(f"missing required file: {REQUIRED_FILES[1]}", errors)
            self.assertIn("broken local link in README.md: absent.md", errors)

    def test_rejects_local_link_that_escapes_repository(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("[outside](../outside.md)\n", encoding="utf-8")

            errors = validate(root)

            self.assertIn("link escapes repository in README.md: ../outside.md", errors)


if __name__ == "__main__":
    unittest.main()
