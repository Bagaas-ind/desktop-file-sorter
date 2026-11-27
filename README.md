# Desktop File Sorter — Windows File Organizer

Desktop File Sorter adalah aplikasi desktop Windows open-source yang dirancang dengan Python untuk merapikan folder Downloads secara nyata, aman, dan terstruktur.

## Fitur Utama
1. **Deteksi Otomatis Folder Downloads**: Otomatis mendeteksi folder Downloads pengguna aktif atau kustomisasi folder target.
2. **Scan & Klasifikasi Ekstensi**: Mengelompokkan file secara otomatis ke folder kategori (PDF, ZIP, JPG, MP4, INSTALLER, dll.).
3. **Pindahan File Nyata**: Memindahkan file asli pada Windows File Explorer secara langsung.
4. **Keamanan Maksimal**: Mencegah overwrite file menggunakan penomoran otomatis `(1)`, mengabaikan file tersembunyi, symbolic link, dan tidak menyentuh folder sistem.
5. **Sistem Undo**: Mengembalikan file ke lokasi semula menggunakan riwayat aktivitas berbasis JSON.
6. **GUI Modern & Non-Blocking**: Dibangun dengan Tkinter dan *threading* agar aplikasi tetap responsif.

## Persyaratan
- Python 3.12 atau kompatibel.
- Sistem Operasi Windows.

## Cara Instalasi & Menjalankan (Development)
1. Clone atau ekstrak folder project **DesktopFileSorter**.
2. Buka Command Prompt (CMD) di dalam folder project.
3. Install dependencies (opsional untuk testing/build):
   ```cmd
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi:
   ```cmd
   python main.py
   ```

## Menjalankan Testing
Untuk menjalankan seluruh unit test dengan direktori sementara:
```cmd
python -m unittest discover tests
```

## Cara Build ke Windows EXE (PyInstaller)
Pastikan PyInstaller telah terpasang, lalu jalankan perintah berikut di CMD:
```cmd
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```
Hasil file executable akan berada di direktori:
`dist/DesktopFileSorter.exe`

## Lokasi Penyimpanan History
Riwayat aktivitas dan pengaturan aplikasi disimpan secara aman di folder:
`%APPDATA%/DesktopFileSorter/`
