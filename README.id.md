<div align="center">

# Desktop File Sorter

### Less clutter. More clarity.

Aplikasi desktop Windows ringan untuk merapikan file berdasarkan ekstensinya.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-2C2C2C?style=flat-square)
![Project](https://img.shields.io/badge/Project-Desktop%20Utility-lightgrey?style=flat-square)

**🌐 Bahasa:** [English](README.md) | Bahasa Indonesia

</div>

---

## Sekilas

Tidak perlu lagi memindahkan file unduhan satu per satu. Desktop File Sorter memindai folder yang dipilih, menampilkan rencana lokasi file, lalu merapikannya setelah kamu memberikan konfirmasi.

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

> **Alur sederhana:** Pilih folder → Pindai → Periksa → Rapikan.

---

## ✨ Fitur

- **Pilih folder** — rapikan folder Downloads atau pilih folder lainnya.
- **Preview sebelum merapikan** — pindai file dan periksa lokasi tujuan sebelum dipindahkan.
- **Pengelompokan otomatis** — file dikelompokkan berdasarkan ekstensi, seperti PDF, ZIP, JPG, DOCX, dan MP4.
- **Pengelompokan installer** — format installer yang didukung dimasukkan ke folder `INSTALLER/`.
- **Perlindungan nama file** — file yang sudah ada tidak ditimpa; aplikasi menambahkan nomor pada nama duplikat (contoh: `laporan (1).pdf`).
- **Riwayat aktivitas** — lihat operasi perapian sebelumnya.
- **Undo** — kembalikan file ke lokasi asal jika lokasi tersebut masih tersedia.
- **Berjalan secara lokal** — tidak memerlukan akun atau layanan online.

## 🖥️ Bagian Aplikasi

| Bagian | Fungsi |
| --- | --- |
| **Dashboard** | Menampilkan folder pilihan dan ringkasan file. |
| **Organize Files** | Memindai file, menampilkan preview, dan memulai perapian setelah konfirmasi. |
| **History** | Melihat riwayat operasi dan menggunakan Undo. |
| **Settings** | Memilih folder dan mengatur konfirmasi. |
| **About** | Menampilkan informasi aplikasi. |

## ⚙️ Teknologi

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Tkinter-2C2C2C?style=flat-square" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white" alt="Windows" />
  <img src="https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white" alt="JSON" />
</div>

Dibangun menggunakan standard library Python, termasuk Tkinter, pathlib, shutil, dan JSON.

## 📦 Persiapan

### Persyaratan

- Windows
- Disarankan Python 3.12
- Tkinter (sudah termasuk dalam instalasi Python standar di Windows)

### Menjalankan dari Source Code

1. Download atau clone repository ini.
2. Ekstrak file ZIP jika mengunduh source code.
3. Buka PowerShell atau Command Prompt di folder proyek (folder yang berisi `main.py`).
4. Jalankan:

```powershell
python main.py
```

Aplikasi utama menggunakan standard library Python. Jika ingin memasang paket yang tercantum di proyek, jalankan:

```powershell
python -m pip install -r requirements.txt
```

## 🚀 Cara Menggunakan

1. Jalankan **Desktop File Sorter**.
2. Buka **Settings** dan periksa folder tujuan. Secara default, aplikasi menggunakan folder Downloads.
3. Untuk memilih folder lain, klik **Browse**, pilih folder, lalu simpan pengaturan.
4. Buka **Organize Files**, kemudian klik **Scan Ulang** untuk memindai folder.
5. Periksa daftar file dan folder tujuan pada preview.
6. Klik **RAPIKAN DOWNLOADS SEKARANG**, lalu konfirmasi prosesnya.
7. Buka **History** untuk melihat riwayat atau mencoba mengembalikan file menggunakan **Undo**.

### Contoh

Sebelum:

```text
Downloads/
├── tugas.pdf
├── foto.zip
├── liburan.jpg
└── installer.exe
```

Sesudah:

```text
Downloads/
├── PDF/
│   └── tugas.pdf
├── ZIP/
│   └── foto.zip
├── JPG/
│   └── liburan.jpg
└── INSTALLER/
    └── installer.exe
```

**Catatan:** Aplikasi hanya memindai file yang berada langsung di dalam folder pilihan. File di dalam subfolder tidak dipindai secara rekursif.

## ↩️ Riwayat dan Undo

Operasi perapian yang berhasil akan disimpan dalam riwayat lokal. Dari menu **History**, pilih operasi lalu klik **Undo** untuk memindahkan file kembali ke lokasi asal.

Undo tidak dapat mengembalikan file jika lokasi asalnya sudah ditempati file lain. Periksa pesan dari aplikasi jika ada file yang gagal dikembalikan.

## 🛡️ Gunakan dengan Aman

- Uji aplikasi terlebih dahulu menggunakan folder sementara yang berisi salinan beberapa file.
- Periksa preview dan dialog konfirmasi sebelum melanjutkan.
- Aplikasi memindahkan file dan tidak sengaja menghapusnya.
- Tetap simpan backup untuk file penting.
- Jangan tutup aplikasi atau matikan Windows saat proses perapian sedang berlangsung.

## 🧪 Menjalankan Pengujian

Dari folder proyek, jalankan:

```powershell
python -m unittest discover -s tests -v
```

## 🏗️ Membuat File Executable Windows (Opsional)

Pasang PyInstaller:

```powershell
python -m pip install pyinstaller
```

Buat file executable:

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

File executable akan dibuat di:

```text
dist/DesktopFileSorter.exe
```

Perintah ini ditujukan untuk developer. File executable siap pakai belum disertakan, kecuali jika dipublikasikan secara terpisah di bagian **Releases** repository.

## 🗂️ Data Aplikasi

Pengaturan aplikasi dan riwayat operasi disimpan secara lokal di:

```text
%APPDATA%/DesktopFileSorter/
```

## 🤝 Kontribusi

Saran, laporan bug, dan kontribusi sangat terbuka. Buat **Issue** untuk melaporkan masalah atau memberikan ide pengembangan, atau kirim **Pull Request** dengan perubahan yang kamu buat.

## ⭐ Dukung Proyek Ini

Jika Desktop File Sorter membantu merapikan foldermu, pertimbangkan untuk memberikan **Star** ⭐ pada repository ini. Dukungan tersebut membantu orang lain menemukan proyek ini dan mendorong pengembangan selanjutnya.

## 📄 Lisensi

Saat ini belum ada lisensi yang ditambahkan. Sebelum lisensi tersedia, kode dalam repository ini belum diberikan lisensi penggunaan ulang open-source. Hubungi pemilik repository sebelum mendistribusikan ulang atau menggunakan kembali kode ini.

---

**Desktop File Sorter**  
*Less clutter. More clarity.*  
Dibuat oleh [Bagaas-ind](https://github.com/Bagaas-ind)
