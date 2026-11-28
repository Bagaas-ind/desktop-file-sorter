<div align="center">

# 🗂️ Desktop File Sorter

### Less clutter. More clarity.

Aplikasi desktop Windows ringan untuk merapikan file secara otomatis ke dalam folder berdasarkan ekstensi file.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-444444?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![MIT License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](LICENSE)

[English](README.md) | **Bahasa Indonesia**

[▶ Tonton Demo](https://github.com/Bagaas-ind/desktop-file-sorter/issues/1) · [Laporkan Bug](https://github.com/Bagaas-ind/desktop-file-sorter/issues) · [Lihat Repository](https://github.com/Bagaas-ind/desktop-file-sorter)

</div>

---

## Apa itu Desktop File Sorter?

Folder Downloads atau Desktop sering kali dipenuhi berbagai jenis file. Desktop File Sorter membantu merapikannya tanpa harus memindahkan file satu per satu secara manual.

Pilih folder, pindai file, periksa preview, lalu konfirmasi. Aplikasi akan memindahkan file yang didukung ke dalam folder sesuai ekstensinya.

### Sebelum dan sesudah

```text
SEBELUM                                 SESUDAH
Downloads/                              Downloads/
├── tugas.pdf                           ├── PDF/
├── foto-liburan.jpg        ─────────▶  │   └── tugas.pdf
├── arsip.zip                           ├── JPG/
└── setup.exe                           │   └── foto-liburan.jpg
                                        ├── ZIP/
                                        │   └── arsip.zip
                                        └── INSTALLER/
                                            └── setup.exe
```

**Alur sederhana:** Pilih folder → Pindai → Periksa → Rapikan.

## Fitur utama

| Fitur | Penjelasan |
| --- | --- |
| Pilih folder | Rapikan folder Downloads secara default atau pilih folder lain. |
| Scan dan preview | Lihat file yang ditemukan beserta folder tujuan sebelum dipindahkan. |
| Pengelompokan otomatis | Kelompokkan file seperti PDF, JPG, ZIP, DOCX, MP4, dan ekstensi lain yang didukung. |
| Pengelompokan installer | Masukkan file installer yang didukung ke folder `INSTALLER`. |
| Perlindungan file duplikat | File yang sudah ada tidak ditimpa; nama file baru akan diberi nomor. |
| Riwayat operasi | Lihat proses perapian yang pernah dilakukan. |
| Undo | Kembalikan file ke lokasi asal selama lokasi tersebut masih tersedia. |
| Proses lokal | File dirapikan langsung di komputer, tanpa akun atau layanan online. |

## Cara menggunakan aplikasi

1. Jalankan aplikasi.
2. Buka **Settings** dan periksa folder yang akan dirapikan. Secara default, aplikasi menggunakan folder **Downloads** Windows.
3. Untuk memilih lokasi lain, klik **Browse**, pilih folder, lalu simpan.
4. Buka **Organize Files**, kemudian klik **Scan Ulang**.
5. Periksa hasil pemindaian dan folder tujuan file.
6. Klik **RAPIKAN DOWNLOADS SEKARANG**, lalu konfirmasi.
7. Buka **History** untuk melihat riwayat atau menggunakan **Undo** jika diperlukan.

> **Penting:** Aplikasi hanya memindai file yang berada langsung di dalam folder pilihan. Isi subfolder tidak dipindai secara rekursif.

## Bagian-bagian aplikasi

| Bagian | Fungsi |
| --- | --- |
| Dashboard | Menampilkan folder pilihan dan ringkasan jumlah file serta kategori. |
| Organize Files | Memindai file, menampilkan preview tujuan, dan menjalankan proses perapian. |
| History | Menampilkan riwayat operasi dan menyediakan fitur Undo. |
| Settings | Mengubah folder tujuan dan pengaturan konfirmasi. |
| About | Menampilkan informasi aplikasi. |

## Instalasi

### Persyaratan

- Windows 10 atau Windows 11.
- Disarankan Python 3.12 atau lebih baru.
- Tkinter (biasanya sudah termasuk dalam installer Python standar untuk Windows).
- Git hanya diperlukan jika memilih metode clone.

### Pilihan 1 — Download ZIP (paling mudah)

1. Buka halaman [repository](https://github.com/Bagaas-ind/desktop-file-sorter).
2. Klik **Code → Download ZIP**.
3. Ekstrak file ZIP.
4. Buka folder hasil ekstrak (folder yang berisi file `main.py`).
5. Buka PowerShell atau Command Prompt di folder tersebut.
6. Jalankan:

```powershell
python main.py
```

### Pilihan 2 — Clone dengan Git

Instal [Python](https://www.python.org/downloads/windows/) dan [Git](https://git-scm.com/download/win) terlebih dahulu. Saat memasang Python, aktifkan opsi **Add Python to PATH**.

Kemudian jalankan:

```powershell
git clone https://github.com/Bagaas-ind/desktop-file-sorter.git
cd desktop-file-sorter
python main.py
```

### Apakah perlu memasang dependency?

Biasanya tidak. Aplikasi menggunakan standard library Python, termasuk Tkinter. Jadi, kamu tidak perlu memasang package tambahan hanya untuk menjalankannya.

File `requirements.txt` berisi tools opsional untuk pengujian dan proses build. Pasang hanya jika dibutuhkan:

```powershell
python -m pip install -r requirements.txt
```

## Keamanan dan hal penting

Baca beberapa catatan ini sebelum merapikan file penting:

- **Periksa preview terlebih dahulu.** Pastikan file dan folder tujuan sudah sesuai sebelum konfirmasi.
- **Coba folder uji.** Mulailah dengan beberapa salinan file di folder sementara.
- **File dipindahkan, bukan sengaja dihapus.** Aplikasi dirancang untuk memindahkan file ke folder kategori.
- **File yang sudah ada dilindungi.** Jika nama file sudah digunakan di folder tujuan, aplikasi menambahkan nomor agar file lama tidak tertimpa.
- **Undo memiliki batasan.** File tidak dapat dikembalikan jika lokasi asalnya sudah ditempati file lain.
- **Tetap simpan backup.** Undo bukan pengganti backup terpisah.
- **Jangan hentikan proses.** Hindari menutup aplikasi atau mematikan Windows saat file sedang dipindahkan.

### File apa saja yang dilewati?

Aplikasi tidak memindai isi subfolder secara rekursif. Aplikasi juga melewati folder, symbolic link, hidden dotfiles, dan beberapa file metadata aplikasi.

### Di mana pengaturan dan riwayat disimpan?

Pengaturan dan riwayat operasi disimpan secara lokal di Windows pada:

```text
%APPDATA%\DesktopFileSorter\
```

Data disimpan secara terpisah untuk setiap akun pengguna Windows.

## Menjalankan pengujian

Jalankan perintah berikut dari folder proyek:

```powershell
python -m unittest discover -s tests -v
```

## Membuat file executable Windows (opsional)

Kamu bisa mengemas aplikasi menjadi file executable menggunakan [PyInstaller](https://pyinstaller.org/):

```powershell
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

Hasilnya akan dibuat di:

```text
dist/DesktopFileSorter.exe
```

Perintah ini digunakan untuk membuat executable sendiri. File `.exe` siap unduh hanya tersedia jika pemilik proyek mempublikasikannya di bagian **Releases**.

## Teknologi yang digunakan

Proyek ini menggunakan teknologi yang ringan dan memanfaatkan fitur bawaan Python sebisa mungkin.

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-444444?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![JSON](https://img.shields.io/badge/Data-JSON-000000?style=flat-square&logo=json&logoColor=white)](https://www.json.org/)
[![PyInstaller](https://img.shields.io/badge/Build-PyInstaller-eeeeee?style=flat-square)](https://pyinstaller.org/)

</div>

| Teknologi | Kegunaan dalam proyek |
| --- | --- |
| **Python** | Bahasa pemrograman utama. |
| **Tkinter** | Membuat tampilan aplikasi desktop (GUI). |
| **pathlib** | Mengelola lokasi file dan folder. |
| **shutil** | Memindahkan file antarfolder. |
| **JSON** | Menyimpan pengaturan dan riwayat secara lokal. |
| **unittest** | Menjalankan pengujian otomatis proyek. |
| **PyInstaller** | Tools opsional untuk mengemas aplikasi menjadi executable Windows. |

## Kontribusi

Saran, laporan bug, dan kontribusi sangat terbuka.

1. Fork repository ini.
2. Buat branch untuk perubahan.
3. Lakukan perubahan dan pengujian.
4. Buat Pull Request dengan penjelasan yang jelas.

Untuk melaporkan bug atau mengusulkan fitur, silakan buat [GitHub Issue](https://github.com/Bagaas-ind/desktop-file-sorter/issues).

## Lisensi

Proyek ini menggunakan [MIT License](LICENSE).

---

<div align="center">

**Desktop File Sorter**  
*Less clutter. More clarity.*

Dibuat oleh [Bagaas-ind](https://github.com/Bagaas-ind)

Jika proyek ini bermanfaat, dukung dengan memberikan ⭐ Star di GitHub.

</div>
