import os
from pathlib import Path
from app.utils import get_category_for_file

class FileScanner:
    def __init__(self, target_dir: Path):
        self.target_dir = Path(target_dir)

    def scan(self) -> list:
        scanned_files = []
        if not self.target_dir.exists() or not self.target_dir.is_dir():
            return scanned_files

        try:
            for item in self.target_dir.iterdir():
                if item.is_dir() or item.is_symlink():
                    continue
                if item.name.startswith('.'):
                    continue
                if item.name.lower() in ['desktopfilesorter_history.json', 'desktopfilesorter_settings.json', 'filetidy_history.json', 'filetidy_settings.json']:
                    continue

                try:
                    file_size = item.stat().st_size
                except (PermissionError, OSError):
                    continue

                category = get_category_for_file(item)
                scanned_files.append({
                    'name': item.name,
                    'path': str(item),
                    'size': file_size,
                    'extension': item.suffix.lower() if item.suffix else '',
                    'category': category,
                    'destination': str(self.target_dir / category / item.name)
                })
        except Exception as e:
            print(f"Error saat scanning: {e}")

        return scanned_files
