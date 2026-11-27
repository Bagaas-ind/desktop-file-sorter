<div align="center">

# Desktop File Sorter

### Less clutter. More clarity.

A lightweight Windows desktop app that organizes your files by extension.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-2C2C2C?style=flat-square)
![Status](https://img.shields.io/badge/Project-Open%20Source%20Ready-lightgrey?style=flat-square)

**🌐 Languages:** English | [Bahasa Indonesia](README.id.md)

</div>

---

## At a Glance

No more manually sorting every download. Desktop File Sorter scans the selected folder, shows where files will go, and organizes them into extension-based folders after confirmation.

```text
 BEFORE                                  AFTER
 Downloads/                              Downloads/
 ├── assignment.pdf                      ├── PDF/
 ├── photos.zip              ───────▶    │   └── assignment.pdf
 ├── vacation.jpg                        ├── ZIP/
 └── installer.exe                       │   └── photos.zip
                                         ├── JPG/
                                         │   └── vacation.jpg
                                         └── INSTALLER/
                                             └── installer.exe
```

> **Simple workflow:** Select folder → Scan → Review → Organize.

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

| Section | What it does |
| --- | --- |
| **Dashboard** | Shows the selected folder and a summary of files. |
| **Organize Files** | Scans files, displays a preview, and starts sorting after confirmation. |
| **History** | Reviews previous operations and provides Undo. |
| **Settings** | Lets you choose the folder and confirmation preference. |
| **About** | Displays application information. |

## ⚙️ Technology

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Tkinter-2C2C2C?style=flat-square" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white" alt="Windows" />
  <img src="https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white" alt="JSON" />
</div>

Built with Python's standard library, including Tkinter, pathlib, shutil, and JSON.

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
