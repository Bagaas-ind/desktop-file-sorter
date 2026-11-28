<div align="center">

# 🗂️ Desktop File Sorter

### Less clutter. More clarity.

A lightweight Windows desktop application that automatically organizes files into folders based on their file extensions.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-444444?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![MIT License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](LICENSE)

**English** | [Bahasa Indonesia](README.id.md)

[▶ Watch Demo](https://github.com/Bagaas-ind/desktop-file-sorter/issues/1) · [Report a Bug](https://github.com/Bagaas-ind/desktop-file-sorter/issues) · [View Repository](https://github.com/Bagaas-ind/desktop-file-sorter)

</div>

---

## What is Desktop File Sorter?

Downloads and desktop folders can quickly become messy. Desktop File Sorter helps you organize them without manually moving files one by one.

Select a folder, scan its files, review the preview, and confirm. The application then moves supported files into folders named after their extensions.

### Before and after

```text
BEFORE                                  AFTER
Downloads/                              Downloads/
├── notes.pdf                           ├── PDF/
├── holiday.jpg            ─────────▶   │   └── notes.pdf
├── archive.zip                         ├── JPG/
└── setup.exe                           │   └── holiday.jpg
                                        ├── ZIP/
                                        │   └── archive.zip
                                        └── INSTALLER/
                                            └── setup.exe
```

**Simple workflow:** Select folder → Scan → Review → Organize.

## Features

| Feature | What it does |
| --- | --- |
| Folder selection | Organize the default Downloads folder or choose another folder. |
| Scan and preview | See detected files and their destination folders before anything moves. |
| Automatic sorting | Group files such as PDF, JPG, ZIP, DOCX, MP4, and other supported extensions. |
| Installer grouping | Put supported installer files into an `INSTALLER` folder. |
| Duplicate protection | Avoid overwriting existing files by adding a number to duplicate filenames. |
| Operation history | Review previous file-organizing operations. |
| Undo | Move files back to their original locations when those locations are available. |
| Local processing | Organize files directly on your computer; no account or online service is required. |

## How to use it

1. Open the application.
2. Go to **Settings** and check the folder you want to organize. The default is your Windows **Downloads** folder.
3. To choose another location, click **Browse**, select a folder, and save.
4. Open **Organize Files** and click **Scan Ulang**.
5. Review the scan results and destination folders.
6. Click **RAPIKAN DOWNLOADS SEKARANG** and confirm.
7. Open **History** to review the operation or use **Undo** if needed.

> **Important:** The app scans files directly inside the selected folder. It does not scan files inside subfolders recursively.

## Application overview

| Section | Purpose |
| --- | --- |
| Dashboard | Shows the selected folder and a summary of files and categories. |
| Organize Files | Scans files, previews destinations, and starts the organizing process. |
| History | Displays previous operations and provides the Undo option. |
| Settings | Lets you change the target folder and confirmation preference. |
| About | Shows application information. |

## Installation

### Requirements

- Windows 10 or Windows 11.
- Python 3.12 or newer recommended.
- Tkinter (normally included with the standard Windows Python installer).
- Git is only required if you choose the clone method.

### Option 1 — Download ZIP (easiest)

1. Open the [repository page](https://github.com/Bagaas-ind/desktop-file-sorter).
2. Click **Code → Download ZIP**.
3. Extract the ZIP file.
4. Open the extracted project folder (the folder containing `main.py`).
5. Open PowerShell or Command Prompt in that folder.
6. Run:

```powershell
python main.py
```

### Option 2 — Clone with Git

First, install [Python](https://www.python.org/downloads/windows/) and [Git](https://git-scm.com/download/win). During Python setup, enable **Add Python to PATH**.

Then run:

```powershell
git clone https://github.com/Bagaas-ind/desktop-file-sorter.git
cd desktop-file-sorter
python main.py
```

### Do I need to install dependencies?

Usually, no. The application uses Python's standard library, including Tkinter. You do not need to install extra packages just to run it.

The `requirements.txt` file contains optional tools for testing and building. Install them only if you need them:

```powershell
python -m pip install -r requirements.txt
```

## Safety and important notes

Please read these points before organizing important files:

- **Preview first.** Always review the detected files and destination folders before confirming.
- **Try a test folder.** Start with copies of a few files in a temporary folder.
- **Files are moved, not intentionally deleted.** The application is designed to move files into category folders.
- **Existing files are protected.** If a filename already exists at the destination, a numbered filename is used instead of overwriting it.
- **Undo has limits.** A file cannot be restored to its original path if that path is already occupied.
- **Keep backups.** Undo is not a replacement for a separate backup.
- **Do not interrupt the process.** Avoid closing the app or shutting down Windows while files are being moved.

### What the app skips

The application does not recursively scan subfolders. It also skips folders, symbolic links, hidden dotfiles, and certain application metadata files.

### Where are settings and history saved?

Settings and operation history are stored locally on Windows at:

```text
%APPDATA%\DesktopFileSorter\
```

The data is stored separately for each Windows user account.

## Run tests

From the project folder, run:

```powershell
python -m unittest discover -s tests -v
```

## Build a Windows executable (optional)

You can package the app into an executable using [PyInstaller](https://pyinstaller.org/):

```powershell
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name DesktopFileSorter main.py
```

The output will be created at:

```text
dist/DesktopFileSorter.exe
```

This command lets you build the executable yourself. A ready-to-download `.exe` is available only if the project owner publishes one in **Releases**.

## Technology stack

The project keeps its stack lightweight and uses Python's built-in tools wherever possible.

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-444444?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![JSON](https://img.shields.io/badge/Data-JSON-000000?style=flat-square&logo=json&logoColor=white)](https://www.json.org/)
[![PyInstaller](https://img.shields.io/badge/Build-PyInstaller-eeeeee?style=flat-square)](https://pyinstaller.org/)

</div>

| Technology | Role in this project |
| --- | --- |
| **Python** | Main programming language. |
| **Tkinter** | Builds the desktop graphical interface (GUI). |
| **pathlib** | Handles file and folder paths. |
| **shutil** | Moves files between folders. |
| **JSON** | Stores local settings and operation history. |
| **unittest** | Runs the project's automated tests. |
| **PyInstaller** | Optional tool for packaging the app as a Windows executable. |

## Contributing

Suggestions, bug reports, and contributions are welcome.

1. Fork this repository.
2. Create a branch for your changes.
3. Make your changes and test them.
4. Open a Pull Request with a clear explanation.

For bugs or feature requests, please open a [GitHub Issue](https://github.com/Bagaas-ind/desktop-file-sorter/issues).

## License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Desktop File Sorter**  
*Less clutter. More clarity.*

Made by [Bagaas-ind](https://github.com/Bagaas-ind)

If this project helps you, consider giving it a ⭐ on GitHub.

</div>
