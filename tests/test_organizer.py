import unittest
import tempfile
from pathlib import Path
from app.organizer import FileOrganizer

class TestOrganizer(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        self.pdf_file = self.test_path / "dokumen.pdf"
        self.exe_file = self.test_path / "aplikasi.exe"
        self.pdf_file.write_text("dummy pdf content")
        self.exe_file.write_text("dummy exe content")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_organize_and_collision_avoidance(self):
        organizer = FileOrganizer(self.test_path)
        success, errors = organizer.organize()
        self.assertEqual(len(success), 2)
        self.assertEqual(len(errors), 0)

        pdf_dest = self.test_path / "PDF" / "dokumen.pdf"
        exe_dest = self.test_path / "INSTALLER" / "aplikasi.exe"
        self.assertTrue(pdf_dest.exists())
        self.assertTrue(exe_dest.exists())

        self.pdf_file.write_text("new pdf content")
        success2, _ = organizer.organize()
        self.assertEqual(len(success2), 1)
        pdf_dest_collision = self.test_path / "PDF" / "dokumen (1).pdf"
        self.assertTrue(pdf_dest_collision.exists())

if __name__ == '__main__':
    unittest.main()
