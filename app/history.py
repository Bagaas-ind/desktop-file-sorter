import json
import os
from datetime import datetime
from pathlib import Path

class HistoryManager:
    def __init__(self):
        self.appdata_dir = Path(os.getenv('APPDATA')) / 'DesktopFileSorter' if os.getenv('APPDATA') else Path.home() / '.desktopfilesorter'
        self.history_file = self.appdata_dir / 'history.json'
        self._ensure_storage()

    def _ensure_storage(self):
        try:
            self.appdata_dir.mkdir(parents=True, exist_ok=True)
            if not self.history_file.exists():
                self._save_data([])
        except Exception:
            pass

    def _load_data(self) -> list:
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return []

    def _save_data(self, data: list):
        try:
            self.appdata_dir.mkdir(parents=True, exist_ok=True)
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Gagal menyimpan riwayat: {e}")

    def add_batch_record(self, target_dir: str, operations: list):
        if not operations:
            return
        
        history = self._load_data()
        batch_record = {
            'id': datetime.now().strftime('%Y%m%d_%H%M%S'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'target_dir': str(target_dir),
            'total_files': len(operations),
            'operations': operations,
            'undone': False
        }
        history.insert(0, batch_record)
        self._save_data(history)

    def get_all_history(self) -> list:
        return self._load_data()

    def mark_as_undone(self, batch_id: str):
        history = self._load_data()
        for item in history:
            if item.get('id') == batch_id:
                item['undone'] = True
                break
        self._save_data(history)
