import tempfile
import unittest
from pathlib import Path

from scripts.validate import REQUIRED_FILES, validate


class ValidateTests(unittest.TestCase):
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
