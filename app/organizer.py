import shutil
from pathlib import Path
from app.scanner import FileScanner

class FileOrganizer:
    def __init__(self, target_dir: Path):
        self.target_dir = Path(target_dir)

    def organize(self, progress_callback=None) -> tuple:
        scanner = FileScanner(self.target_dir)
        files = scanner.scan()
        
        success_ops = []
        error_ops = []

        total = len(files)
        for index, file_info in enumerate(files):
            src_path = Path(file_info['path'])
            category = file_info['category']
            
            dest_dir = self.target_dir / category
            dest_path = dest_dir / src_path.name

            try:
                dest_dir.mkdir(parents=True, exist_ok=True)
                final_dest_path = dest_path
                counter = 1
                while final_dest_path.exists():
                    stem = src_path.stem
                    suffix = src_path.suffix
                    new_name = f"{stem} ({counter}){suffix}"
                    final_dest_path = dest_dir / new_name
                    counter += 1

                shutil.move(str(src_path), str(final_dest_path))

                op_record = {
                    'filename': src_path.name,
                    'original_path': str(src_path),
                    'new_path': str(final_dest_path),
                    'category': category
                }
                success_ops.append(op_record)

            except Exception as e:
                error_ops.append({
                    'filename': src_path.name,
                    'path': str(src_path),
                    'error': str(e)
                })

            if progress_callback:
                progress_callback(index + 1, total, src_path.name)

        return success_ops, error_ops

    @staticmethod
    def undo_operation(operation_record: list, progress_callback=None) -> tuple:
        success_undo = []
        error_undo = []

        total = len(operation_record)
        for index, record in enumerate(operation_record):
            current_path = Path(record['new_path'])
            original_path = Path(record['original_path'])

            try:
                if current_path.exists():
                    if original_path.exists():
                        error_undo.append({
                            'filename': record['filename'],
                            'reason': 'Lokasi awal sudah terisi file lain.'
                        })
                    else:
                        original_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(current_path), str(original_path))
                        success_undo.append(record)
                else:
                    error_undo.append({
                        'filename': record['filename'],
                        'reason': 'File di lokasi tujuan sudah tidak ditemukan.'
                    })
            except Exception as e:
                error_undo.append({
                    'filename': record['filename'],
                    'reason': str(e)
                })

            if progress_callback:
                progress_callback(index + 1, total, record['filename'])

        return success_undo, error_undo
