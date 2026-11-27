<div align="center">

# Desktop File Sorter

### Less clutter. More clarity.

Aplikasi desktop Windows sederhana untuk merapikan file ke dalam folder berdasarkan ekstensinya.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-444444?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**Bahasa:** [English](README.md) | Bahasa Indonesia

</div>

---




## Tentang Proyek

Desktop File Sorter membantu merapikan folder tanpa harus memindahkan setiap file secara manual. Aplikasi memindai folder yang kamu pilih, menampilkan preview lokasi tujuan, lalu memindahkan file ke folder berdasarkan ekstensinya setelah kamu memberikan konfirmasi.

```text
 SEBELUM                                 SESUDAH
 Downloads/                              Downloads/
 ├── tugas.pdf                           ├── PDF/
 ├── foto.zip                 ───────▶   │   └── tugas.pdf
 ├── liburan.jpg                         ├── ZIP/
 └── installer.exe                       │   └── foto.zip
                                         ├── JPG/
                                         │   └── liburan.jpg
                                         └── INSTALLER/
                                             └── installer.exe
```

**Alur penggunaan:** Pilih folder → Pindai → Periksa → Rapikan.

## Fitur

- **Pilih folder** — secara default menggunakan Downloads atau kamu bisa memilih folder lain.
- **Preview sebelum merapikan** — periksa file yang ditemukan dan folder tujuan sebelum dipindahkan.
- **Pengelompokan otomatis** — kelompokkan file berdasarkan ekstensi, seperti PDF, ZIP, JPG, DOCX, MP4, dan lainnya.
- **Pengelompokan installer** — format installer yang didukung dimasukkan ke folder `INSTALLER/`.
- **Perlindungan nama file** — file yang sudah ada tidak ditimpa; nomor ditambahkan pada nama file duplikat, misalnya `laporan (1).pdf`.
- **Riwayat operasi** — lihat proses perapian sebelumnya.
- **Undo** — kembalikan file ke lokasi asal jika lokasi tersebut masih tersedia.
- **Berjalan secara lokal** — proses perapian dilakukan di komputer masing-masing tanpa akun atau layanan online.

## Bagian Aplikasi

| Bagian | Fungsi |
| --- | --- |
| **Dashboard** | Menampilkan folder pilihan dan ringkasan file serta kategori. |
| **Organize Files** | Memindai file, menampilkan preview, dan memulai perapian setelah konfirmasi. |
| **History** | Melihat riwayat operasi dan menggunakan Undo. |
| **Settings** | Mengubah folder tujuan dan pengaturan konfirmasi. |
| **About** | Menampilkan informasi aplikasi. |

## Persyaratan

- Windows 10 atau Windows 11.
- Disarankan Python 3.12 atau lebih baru.
- Tkinter, biasanya sudah termasuk dalam installer Python standar untuk Windows.
- Git jika ingin melakukan clone repository melalui terminal.

> Kamu tidak memerlukan akun GitHub untuk melakukan clone repository publik ini. Git hanya diperlukan untuk metode Git Clone. Kamu juga bisa mengunduh proyek sebagai file ZIP.

## Instalasi dan Menjalankan Aplikasi

Pilih **salah satu** dari dua metode berikut.

### Metode 1 — Clone dengan Git

1. Instal Python dari [python.org](https://www.python.org/downloads/windows/). Saat instalasi, aktifkan opsi **Add Python to PATH**.
2. Instal Git dari [git-scm.com](https://git-scm.com/download/win).
3. Buka PowerShell atau Command Prompt.
4. Jalankan perintah berikut:

```powershell
git clone https://github.com/Bagaas-ind/desktop-file-sorter.git
cd desktop-file-sorter
python main.py
```

### Metode 2 — Download ZIP

1. Buka [repository Desktop File Sorter](https://github.com/Bagaas-ind/desktop-file-sorter).
2. Klik **Code → Download ZIP**.
3. Ekstrak file ZIP yang sudah diunduh.
4. Buka folder hasil ekstrak `desktop-file-sorter`.
5. Buka PowerShell atau Command Prompt di folder tersebut (folder yang berisi `main.py`).
6. Jalankan:

```powershell
python main.py
```

### Apakah perlu memasang package Python?

Aplikasi utamanya menggunakan standard library Python, termasuk Tkinter. Jadi, biasanya kamu **tidak perlu memasang package tambahan** hanya untuk menjalankan aplikasi.

File `requirements.txt` berisi tools tambahan untuk kebutuhan pengembangan dan build. Pasang hanya jika diperlukan:

```powershell
python -m pip install -r requirements.txt
```

## Penggunaan Pertama

1. Jalankan aplikasi dengan perintah `python main.py`.
2. Buka **Settings** dan periksa folder tujuan. Secara default, aplikasi menggunakan folder Downloads milik akun Windows yang sedang digunakan.
3. Jika ingin merapikan folder lain, klik **Browse**, pilih folder, lalu simpan pengaturan.
4. Buka **Organize Files**, kemudian klik **Scan Ulang**.
5. Periksa daftar file dan folder tujuan pada preview.
6. Klik **RAPIKAN DOWNLOADS SEKARANG**, lalu konfirmasi.
7. Buka **History** untuk melihat riwayat atau menggunakan **Undo** jika ingin mengembalikan file.

### Penting: aplikasi merapikan folder yang dipilih

Aplikasi hanya memindai file yang berada langsung di dalam folder pilihan. Isi subfolder tidak dipindai secara rekursif. Aplikasi melewati folder, symbolic link, file tersembunyi yang namanya diawali titik, dan beberapa file metadata aplikasi.

### Di mana pengaturan dan riwayat disimpan?

Di Windows, pengaturan aplikasi dan riwayat operasi disimpan secara lokal di:

```text
%APPDATA%\DesktopFileSorter\
```

Data ini terpisah untuk setiap akun pengguna Windows.

## Keamanan dan Batasan

Proses perapian memindahkan file dari lokasi awal ke folder kategori. Baca catatan berikut sebelum menggunakannya pada folder penting:

- **Uji terlebih dahulu.** Coba aplikasi menggunakan folder sementara yang berisi salinan beberapa file.
- **Periksa sebelum konfirmasi.** Pastikan preview dan dialog konfirmasi sudah sesuai sebelum memindahkan file.
- **Tidak dirancang untuk menghapus file.** Aplikasi memindahkan file, bukan sengaja menghapusnya.
- **Nama file bentrok.** Jika file dengan nama yang sama sudah ada di folder tujuan, aplikasi menambahkan nomor pada nama file baru agar file lama tidak tertimpa.
- **Batasan Undo.** Undo tidak dapat mengembalikan file jika lokasi asalnya sudah ditempati file lain. Periksa pesan error jika ada file yang gagal dikembalikan.
- **Tetap simpan backup.** Simpan salinan terpisah untuk data penting. Undo bukan pengganti backup.
- **Jangan hentikan proses.** Hindari menutup aplikasi atau mematikan Windows saat file sedang dipindahkan.

## Pengujian

Jalankan pengujian dari folder proyek:

```powershell
python -m unittest discover -s tests -v
```

## Membuat File Executable Windows (Opsional)

Jika ingin mengemas aplikasi menjadi file executable, pasang PyInstaller:

```powershell
python -m pip install pyinstaller
```

Kemudian jalankan:

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

File executable akan dibuat di:

```text
dist/DesktopFileSorter.exe
```

Instruksi ini ditujukan bagi pengguna/developer yang ingin membuat executable sendiri. File `.exe` siap pakai hanya tersedia jika pemilik repository mempublikasikannya di bagian **Releases**.

## Pemecahan Masalah

| Masalah | Solusi yang bisa dicoba |
| --- | --- |
| `python` tidak dikenali | Instal ulang Python dan aktifkan **Add Python to PATH**, atau coba perintah `py main.py`. |
| `git` tidak dikenali | Instal Git, buka ulang terminal, lalu coba kembali. |
| `can't open file 'main.py'` | Pastikan terminal berada di folder proyek hasil clone/ekstrak yang berisi `main.py`. |
| Aplikasi tidak terbuka | Pastikan Python terpasang dengan benar dan Tkinter tersedia. |
| Ada file yang tidak berpindah | Periksa izin akses file, apakah file sedang digunakan aplikasi lain, dan pesan error dari aplikasi. |

## Teknologi

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- pathlib dan shutil
- JSON untuk menyimpan pengaturan dan riwayat secara lokal

## Kontribusi

Kontribusi sangat terbuka.

1. Fork repository ini.
2. Buat branch untuk perubahan yang ingin kamu kerjakan.
3. Lakukan perubahan dan pengujian.
4. Kirim Pull Request dengan penjelasan yang jelas.

Untuk laporan bug atau ide fitur, buat [GitHub Issue](https://github.com/Bagaas-ind/desktop-file-sorter/issues).

## Lisensi

Proyek ini menggunakan **MIT License**. Kamu diperbolehkan menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, memberi sublisensi, dan menjual salinan perangkat lunak ini sesuai ketentuan pada file [LICENSE](LICENSE).

## Dukung Proyek

Jika proyek ini bermanfaat, pertimbangkan untuk memberikan ⭐ Star pada repository. Dukungan tersebut membantu orang lain menemukan Desktop File Sorter.

---

<div align="center">

**Desktop File Sorter**  
*Less clutter. More clarity.*  
Dibuat oleh [Bagaas-ind](https://github.com/Bagaas-ind)

</div>
