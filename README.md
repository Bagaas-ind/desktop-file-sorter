# Desktop File Sorter

**Clean up your folders. Find your files faster.**

A simple Windows desktop app that automatically organizes files into folders based on their file extensions. Scan a folder, review the preview, and let Desktop File Sorter handle the sorting.

> PDF files go to `PDF/`, ZIP files to `ZIP/`, JPG files to `JPG/`, and so on.

**🌐 Languages:** English | [Bahasa Indonesia](README.id.md)

---

## ✨ Features

- **Choose a folder** — organize Downloads or select another folder.
- **Preview before sorting** — scan files and review their planned destinations.
- **Automatic organization** — group files by extension, such as PDF, ZIP, JPG, DOCX, and MP4.
- **Installer grouping** — supported installer packages are placed in `INSTALLER/`.
- **Collision protection** — existing files are not overwritten; a number is added to duplicate names (for example, `report (1).pdf`).
- **Activity history** — review previous sorting operations.
- **Undo** — move files back to their original locations when those locations are available.
- **Works locally** — no account or online service is required.

## 🖥️ App Sections

- **Dashboard** — see the selected folder and a summary of files.
- **Organize Files** — scan, preview, and confirm file organization.
- **History** — review previous operations and use Undo.
- **Settings** — choose the folder to organize and confirmation preference.
- **About** — view application information.

## 📦 Getting Started

### Requirements

- Windows
- Python 3.12 recommended
- Tkinter (included with standard Windows Python installations)

### Run from Source

1. Download or clone this repository.
2. Extract the ZIP archive if you downloaded the source.
3. Open PowerShell or Command Prompt in the project folder (the folder containing `main.py`).
4. Run:

```powershell
python main.py
```

The main application uses Python's standard library. To install the packages listed in the project, run:

```powershell
python -m pip install -r requirements.txt
```

## 🚀 How to Use

1. Launch **Desktop File Sorter**.
2. Open **Settings** and check the target folder. By default, it uses your Downloads folder.
3. To choose another folder, click **Browse**, select the folder, and save the settings.
4. Open **Organize Files** and click **Scan Ulang** to scan the selected folder.
5. Review the file list and destination folders.
6. Click **RAPIKAN DOWNLOADS SEKARANG** and confirm the operation.
7. Open **History** to review the operation or try to restore files with **Undo**.

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

**Note:** The app scans files directly inside the selected folder. It does not scan files inside subfolders recursively.

## ↩️ History and Undo

Successful sorting operations are recorded in local history. From **History**, select an operation and choose **Undo** to move files back to their original locations.

Undo cannot restore a file if another file already occupies its original path. Check the messages shown by the app if some files cannot be restored.

## 🛡️ Use Safely

- Test the app first with a temporary folder containing copies of a few files.
- Review the preview and confirmation dialog before proceeding.
- The app moves files; it does not intentionally delete them.
- Keep backups of important files.
- Do not close the app or shut down Windows while a sorting operation is in progress.

## 🧪 Run Tests

From the project folder, run:

```powershell
python -m unittest discover -s tests -v
```

## 🏗️ Build a Windows Executable (Optional)

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build the executable:

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

The executable will be created at:

```text
dist/DesktopFileSorter.exe
```

This command is for developers. A prebuilt executable is not included unless it is published separately in the repository's **Releases**.

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

## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome. Open an **Issue** to report a problem or suggest an improvement, or submit a **Pull Request** with your changes.

## ⭐ Support the Project

If Desktop File Sorter helps keep your folders organized, consider giving this repository a **Star** ⭐. It helps others discover the project and supports continued development.

## 📄 License

No license has been added yet. Until a license is provided, the code is not granted an open-source reuse license. Please contact the repository owner before redistributing or reusing it.

---

**Desktop File Sorter**  
*Less clutter. More clarity.*  
Made by [Bagaas-ind](https://github.com/Bagaas-ind)
