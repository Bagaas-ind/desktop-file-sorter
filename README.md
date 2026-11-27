# Desktop File Sorter

**Clean up your folders. Find your files faster.**

Desktop File Sorter is a simple Windows desktop app that helps organize a cluttered folder by moving files into folders based on their file extensions. Instead of sorting files manually, scan a folder, review the list, and let Desktop File Sorter do the work.

> **Your files, organized by type.** PDF files go to `PDF/`, ZIP files to `ZIP/`, JPG files to `JPG/`, and so on.

---

## ✨ Features

- **Choose a folder** — use your Downloads folder or select another folder.
- **Scan before sorting** — see the files found and their planned destination.
- **Sort by extension** — files are grouped into folders such as `PDF`, `ZIP`, `JPG`, `DOCX`, and `MP4`.
- **Installer grouping** — supported installer packages are grouped in `INSTALLER/`.
- **Avoid filename overwrites** — when a destination filename already exists, the app adds a number, such as `report (1).pdf`.
- **Activity history** — review previous sorting operations.
- **Undo** — restore files to their original locations from the History page, when those locations are available.
- **Local desktop app** — built with Python and Tkinter. No account or online service is required.

## 🖥️ Preview

The app includes these sections:

- **Dashboard** — view the selected folder and a summary of files and categories.
- **Organize Files** — scan files, review the preview, and confirm sorting.
- **History** — view previous operations and use Undo.
- **Settings** — choose the target folder and confirmation preference.
- **About** — view application information.

## 📦 Getting Started

### Requirements

- Windows
- Python 3.12 recommended
- Tkinter (included with standard Windows Python installations)

### Run from source

1. Download or clone this repository.
2. Extract the project ZIP if you downloaded the source archive.
3. Open PowerShell or Command Prompt in the project folder (the folder containing `main.py`).
4. Start the application:

```powershell
python main.py
```

The project currently uses Python's standard library for its main application features. If you want to install the packages listed by the project, run:

```powershell
python -m pip install -r requirements.txt
```

## 🚀 How to Use

1. Open **Desktop File Sorter**.
2. Go to **Settings** and check the target folder. By default, the app uses your user's Downloads folder.
3. If you want to organize a different folder, click **Browse**, choose the folder, and save the settings.
4. Open **Organize Files** and click **Scan Ulang** to scan the selected folder.
5. Review the file list and destination folders.
6. Click **RAPIKAN DOWNLOADS SEKARANG** and confirm the operation.
7. Open **History** if you want to review the operation or try to restore files using **Undo**.

### Example

Before:

```text
Downloads/
├── assignment.pdf
├── photos.zip
├── vacation.jpg
└── installer.exe
```

After:

```text
Downloads/
├── PDF/
│   └── assignment.pdf
├── ZIP/
│   └── photos.zip
├── JPG/
│   └── vacation.jpg
└── INSTALLER/
    └── installer.exe
```

The app scans files directly inside the selected folder; it does not recursively scan files inside its subfolders.

## ↩️ History and Undo

Each successful sorting operation is recorded in the app's local history. From **History**, select an operation and choose **Undo** to move its files back to their original locations.

Undo cannot restore a file to its original path if another file already occupies that path. Check any messages shown by the app if some files cannot be restored.

## 🛡️ Use Safely

- **Try a test folder first.** Create a temporary folder with copies of a few files and test the workflow before organizing important folders.
- Review the preview and confirmation dialog before proceeding.
- The app moves files; it does not intentionally delete them.
- Keep backups of important files. No file-management tool can replace a backup.
- Do not close the app or shut down Windows while a sorting operation is in progress.

## 🧪 Run Tests

From the project folder, run:

```powershell
python -m unittest discover -s tests -v
```

## 🏗️ Build a Windows Executable (Optional)

To package the application as a Windows executable, install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Then run:

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

The executable will be created at:

```text
dist/DesktopFileSorter.exe
```

This build command is provided for developers. A prebuilt executable is not included unless it is published separately in the repository's **Releases**.

## 🗂️ App Data

Application settings and operation history are stored locally under:

```text
%APPDATA%/DesktopFileSorter/
```

## 🛠️ Built With

- Python
- Tkinter
- pathlib
- shutil
- JSON

## 🌐 Bahasa Indonesia

### Tentang Desktop File Sorter

Desktop File Sorter adalah aplikasi desktop Windows sederhana untuk membantu merapikan folder yang berantakan. Aplikasi ini memindahkan file ke folder berdasarkan ekstensi file, sehingga kamu tidak perlu mengelompokkannya satu per satu secara manual.

**PDF masuk ke folder PDF, ZIP ke folder ZIP, JPG ke folder JPG, dan seterusnya.**

### Fitur

- Memilih folder Downloads atau folder lain.
- Memindai file dan menampilkan preview sebelum dipindahkan.
- Mengelompokkan file berdasarkan ekstensi.
- Menggabungkan file installer yang didukung ke folder `INSTALLER/`.
- Menghindari nama file tertimpa dengan menambahkan nomor, misalnya `laporan (1).pdf`.
- Menyimpan riwayat aktivitas.
- Menyediakan fitur Undo untuk mengembalikan file ke lokasi semula jika lokasi tersebut masih tersedia.
- Berjalan secara lokal di Windows menggunakan Python dan Tkinter.

### Cara Menjalankan

1. Download ZIP repository ini, lalu ekstrak.
2. Buka folder proyek yang berisi file `main.py`.
3. Buka PowerShell atau CMD di folder tersebut.
4. Jalankan:

```powershell
python main.py
```

### Cara Menggunakan

1. Buka Desktop File Sorter.
2. Masuk ke **Settings** dan periksa folder tujuan. Secara default, aplikasi menggunakan folder Downloads pengguna.
3. Untuk memilih folder lain, klik **Browse**, pilih folder, lalu simpan pengaturan.
4. Buka **Organize Files**, kemudian klik **Scan Ulang**.
5. Periksa daftar file dan folder tujuan pada preview.
6. Klik **RAPIKAN DOWNLOADS SEKARANG**, lalu konfirmasi.
7. Buka menu **History** jika ingin melihat riwayat atau menggunakan fitur **Undo**.

### Catatan Keamanan

- Coba terlebih dahulu menggunakan folder percobaan yang berisi salinan file.
- Periksa preview sebelum menyetujui pemindahan.
- Aplikasi memindahkan file, bukan sengaja menghapusnya.
- Fitur Undo tidak dapat mengembalikan file jika lokasi asalnya sudah ditempati file lain.
- Aplikasi hanya memindai file yang berada langsung di dalam folder pilihan, bukan isi subfolder secara rekursif.
- Tetap simpan backup untuk file penting.

---

## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome. Feel free to open an **Issue** to report a problem or suggest an improvement, or submit a **Pull Request** with your changes.

## ⭐ Support the Project

If Desktop File Sorter helps you keep your folders organized, consider giving this repository a **Star** ⭐. It helps other people discover the project and encourages continued development.

## 📄 License

No license has been added yet. Until a license is provided, the repository's code is not granted an open-source reuse license. Please contact the repository owner before redistributing or reusing the code.

---

**Desktop File Sorter**  
*Less clutter. More clarity.*  
Made by [Bagaas-ind](https://github.com/Bagaas-ind)
