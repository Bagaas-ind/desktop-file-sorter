import unittest
import tempfile
from pathlib import Path
from app.scanner import FileScanner

class TestScanner(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        (self.test_path / "sample.pdf").touch()
        (self.test_path / "sample.zip").touch()
        (self.test_path / ".hidden_file.txt").touch()
        sub_folder = self.test_path / "subfolder"
        sub_folder.mkdir()
        (sub_folder / "inner.txt").touch()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_scanner_detection(self):
        scanner = FileScanner(self.test_path)
        files = scanner.scan()
        file_names = [f['name'] for f in files]
        self.assertIn("sample.pdf", file_names)
        self.assertIn("sample.zip", file_names)
        self.assertNotIn(".hidden_file.txt", file_names)
        self.assertNotIn("inner.txt", file_names)

if __name__ == '__main__':
    unittest.main()
