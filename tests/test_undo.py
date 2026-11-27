import unittest
import tempfile
from pathlib import Path
from app.organizer import FileOrganizer

class TestUndo(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        self.sample_file = self.test_path / "laporan.xlsx"
        self.sample_file.write_text("excel data")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_undo_restoration(self):
        organizer = FileOrganizer(self.test_path)
        success, _ = organizer.organize()
        self.assertTrue((self.test_path / "XLSX" / "laporan.xlsx").exists())
        self.assertFalse(self.sample_file.exists())

        success_undo, errors_undo = FileOrganizer.undo_operation(success)
        self.assertEqual(len(success_undo), 1)
        self.assertEqual(len(errors_undo), 0)
        self.assertTrue(self.sample_file.exists())
        self.assertFalse((self.test_path / "XLSX" / "laporan.xlsx").exists())

if __name__ == '__main__':
    unittest.main()
