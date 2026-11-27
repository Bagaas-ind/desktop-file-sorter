import json
import os
from pathlib import Path
from app.utils import get_default_downloads_dir

class SettingsManager:
    def __init__(self):
        self.appdata_dir = Path(os.getenv('APPDATA')) / 'DesktopFileSorter' if os.getenv('APPDATA') else Path.home() / '.desktopfilesorter'
        self.settings_file = self.appdata_dir / 'settings.json'
        self.settings = self._load_settings()

    def _load_settings(self) -> dict:
        default_settings = {
            'target_folder': str(get_default_downloads_dir()),
            'show_confirmation': True
        }
        try:
            if self.settings_file.exists():
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    default_settings.update(data)
        except Exception:
            pass
        return default_settings

    def save_settings(self):
        try:
            self.appdata_dir.mkdir(parents=True, exist_ok=True)
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Gagal menyimpan settings: {e}")

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()
