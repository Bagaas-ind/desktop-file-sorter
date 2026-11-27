import tkinter as tk
from app.gui import DesktopFileSorterApp

def main():
    root = tk.Tk()
    app = DesktopFileSorterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
