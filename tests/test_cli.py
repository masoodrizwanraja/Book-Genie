import json
import tempfile
import unittest
from pathlib import Path

from book_genie.cli import check_project, init_project, main


class ProjectTests(unittest.TestCase):
    def test_create_and_check(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "book"
            init_project(project, "Sample", "Author")
            self.assertEqual(check_project(project), [])
            self.assertEqual(main(["check", str(project)]), 0)
            with self.assertRaises(ValueError):
                init_project(project, "Replacement")

    def test_missing_and_duplicate_chapters(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "book"
            init_project(project, "Sample")
            manifest = project / "book.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            data["chapters"].append(dict(data["chapters"][0]))
            manifest.write_text(json.dumps(data), encoding="utf-8")
            errors = check_project(project)
            self.assertTrue(any("duplicate id" in error for error in errors))
            self.assertTrue(any("number must be 2" in error for error in errors))
            (project / "chapters" / "01-untitled.md").unlink()
            self.assertTrue(any("Missing chapter file" in error for error in check_project(project)))

    def test_rejects_path_escape_and_bad_json(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "book"
            init_project(project, "Sample")
            manifest = project / "book.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            data["chapters"][0]["file"] = "../outside.md"
            manifest.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("under chapters/" in error for error in check_project(project)))
            manifest.write_text("{", encoding="utf-8")
            self.assertTrue(any("Cannot read" in error for error in check_project(project)))


if __name__ == "__main__":
    unittest.main()
