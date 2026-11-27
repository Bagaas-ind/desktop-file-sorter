import os
from pathlib import Path

EXTENSION_MAPPING = {
    '.pdf': 'PDF', '.doc': 'DOC', '.docx': 'DOCX', '.xls': 'XLS', '.xlsx': 'XLSX',
    '.ppt': 'PPT', '.pptx': 'PPTX', '.txt': 'TXT', '.csv': 'CSV', '.rtf': 'RTF',
    '.zip': 'ZIP', '.rar': 'RAR', '.7z': '7Z', '.tar': 'TAR', '.gz': 'GZ',
    '.jpg': 'JPG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF', '.webp': 'WEBP',
    '.svg': 'SVG', '.bmp': 'BMP',
    '.mp4': 'MP4', '.mkv': 'MKV', '.mov': 'MOV', '.avi': 'AVI', '.wmv': 'WMV', '.flv': 'FLV',
    '.mp3': 'MP3', '.wav': 'WAV', '.flac': 'FLAC', '.aac': 'AAC', '.ogg': 'OGG',
    '.php': 'PHP', '.js': 'JS', '.html': 'HTML', '.css': 'CSS', '.py': 'PY',
    '.java': 'JAVA', '.cpp': 'CPP', '.c': 'C', '.sql': 'SQL', '.json': 'JSON',
    '.xml': 'XML', '.ts': 'TS',
    '.exe': 'INSTALLER', '.msi': 'INSTALLER', '.msix': 'INSTALLER', '.appx': 'INSTALLER',
    '.appxbundle': 'INSTALLER', '.msu': 'INSTALLER', '.msp': 'INSTALLER', '.dmg': 'INSTALLER',
    '.pkg': 'INSTALLER', '.deb': 'INSTALLER', '.rpm': 'INSTALLER',
}

def get_category_for_file(file_path: Path) -> str:
    if not file_path.suffix:
        return "TANPA_EKSTENSI"
    ext = file_path.suffix.lower()
    if ext in EXTENSION_MAPPING:
        return EXTENSION_MAPPING[ext]
    return ext[1:].upper()

def get_default_downloads_dir() -> Path:
    return Path.home() / "Downloads"
