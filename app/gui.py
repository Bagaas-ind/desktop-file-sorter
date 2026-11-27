import threading
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from app.scanner import FileScanner
from app.organizer import FileOrganizer
from app.history import HistoryManager
from app.settings import SettingsManager

class DesktopFileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop File Sorter — Windows File Organizer")
        self.root.geometry("950x600")
        self.root.minsize(800, 500)

        self.settings = SettingsManager()
        self.history_mgr = HistoryManager()
        self.target_dir = Path(self.settings.get('target_folder'))
        
        self.scanned_files = []

        self.setup_styles()
        self.create_layout()
        self.show_frame("Dashboard")
        self.refresh_dashboard()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        self.bg_color = "#F8F9FA"
        self.sidebar_color = "#FFFFFF"
        self.accent_color = "#0D6EFD"
        self.text_color = "#212529"
        
        self.root.configure(bg=self.bg_color)
        
        style.configure('.', background=self.bg_color, foreground=self.text_color, font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'), background=self.accent_color, foreground='white')
        style.map('Accent.TButton', background=[('active', '#0b5ed7')])

    def create_layout(self):
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.sidebar = tk.Frame(self.root, bg="#FFFFFF", width=200, relief="flat")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)

        tk.Label(self.sidebar, text="Desktop File Sorter", font=('Segoe UI', 13, 'bold'), bg="#FFFFFF", fg=self.accent_color).pack(pady=20)
        
        nav_items = ["Dashboard", "Organize Files", "History", "Settings", "About"]
        self.frames = {}

        for item in nav_items:
            btn = tk.Button(
                self.sidebar, text=item, font=('Segoe UI', 11), bg="#FFFFFF", fg="#495057",
                activebackground="#E9ECEF", bd=0, anchor="w", padx=20, pady=10,
                command=lambda name=item: self.show_frame(name)
            )
            btn.pack(fill="x", padx=10, pady=2)

        self.frames["Dashboard"] = self.create_dashboard_view()
        self.frames["Organize Files"] = self.create_organize_view()
        self.frames["History"] = self.create_history_view()
        self.frames["Settings"] = self.create_settings_view()
        self.frames["About"] = self.create_about_view()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        if name == "History":
            self.refresh_history_list()
        elif name == "Dashboard":
            self.refresh_dashboard()

    def create_dashboard_view(self):
        frame = tk.Frame(self.content_frame, bg=self.bg_color)
        tk.Label(frame, text="Dashboard", font=('Segoe UI', 18, 'bold'), bg=self.bg_color).pack(anchor="w", pady=(0, 10))
        
        self.lbl_target = tk.Label(frame, text=f"Target Folder: {self.target_dir}", font=('Segoe UI', 11), bg=self.bg_color, fg="#6C757D")
        self.lbl_target.pack(anchor="w", pady=(0, 20))

        cards_frame = tk.Frame(frame, bg=self.bg_color)
        cards_frame.pack(fill="x", pady=10)

        self.lbl_total_files = self.create_card(cards_frame, "Total Files", "0", 0)
        self.lbl_total_categories = self.create_card(cards_frame, "Total Categories", "0", 1)

        btn_frame = tk.Frame(frame, bg=self.bg_color)
        btn_frame.pack(anchor="w", pady=30)

        ttk.Button(btn_frame, text="Scan Files Sekarang", command=self.run_scan_thread, style='Accent.TButton').pack(side="left", padx=(0, 10))
        ttk.Button(btn_frame, text="Buka Folder di Explorer", command=self.open_folder_explorer).pack(side="left")

        return frame

    def create_card(self, parent, title, value, col):
        card = tk.Frame(parent, bg="white", bd=1, relief="solid", padx=20, pady=15)
        card.grid(row=0, column=col, padx=(0, 15), sticky="ew")
        
        tk.Label(card, text=title, font=('Segoe UI', 10), bg="white", fg="#6C757D").pack(anchor="w")
        lbl_val = tk.Label(card, text=value, font=('Segoe UI', 20, 'bold'), bg="white", fg=self.accent_color)
        lbl_val.pack(anchor="w", pady=(5, 0))
        return lbl_val

    def refresh_dashboard(self):
        scanner = FileScanner(self.target_dir)
        files = scanner.scan()
        categories = set(f['category'] for f in files)
        self.lbl_total_files.config(text=str(len(files)))
        self.lbl_total_categories.config(text=str(len(categories)))
        self.lbl_target.config(text=f"Target Folder: {self.target_dir}")

    def create_organize_view(self):
        frame = tk.Frame(self.content_frame, bg=self.bg_color)
        tk.Label(frame, text="Preview & Organize Files", font=('Segoe UI', 18, 'bold'), bg=self.bg_color).pack(anchor="w", pady=(0, 10))

        top_ctrl = tk.Frame(frame, bg=self.bg_color)
        top_ctrl.pack(fill="x", pady=(0, 10))
        ttk.Button(top_ctrl, text="Scan Ulang", command=self.run_scan_thread).pack(side="left", padx=(0, 10))
        self.btn_organize = ttk.Button(top_ctrl, text="RAPIKAN DOWNLOADS SEKARANG", command=self.run_organize_thread, style='Accent.TButton')
        self.btn_organize.pack(side="left")

        tree_frame = tk.Frame(frame, bg=self.bg_color)
        tree_frame.pack(fill="both", expand=True, pady=10)

        columns = ("name", "size", "ext", "category", "dest")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("name", text="Nama File")
        self.tree.heading("size", text="Ukuran (Bytes)")
        self.tree.heading("ext", text="Ekstensi")
        self.tree.heading("category", text="Kategori")
        self.tree.heading("dest", text="Folder Tujuan")

        self.tree.column("name", width=250)
        self.tree.column("size", width=100)
        self.tree.column("ext", width=80)
        self.tree.column("category", width=100)
        self.tree.column("dest", width=300)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return frame

    def run_scan_thread(self):
        def task():
            scanner = FileScanner(self.target_dir)
            self.scanned_files = scanner.scan()
            self.root.after(0, self.update_treeview)
        threading.Thread(target=task, daemon=True).start()

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for f in self.scanned_files:
            self.tree.insert("", "end", values=(f['name'], f['size'], f['extension'], f['category'], f['destination']))

    def run_organize_thread(self):
        if not self.scanned_files:
            messagebox.showinfo("Informasi", "Tidak ada file untuk dirapikan atau belum dilakukan scan.")
            return

        if self.settings.get('show_confirmation', True):
            if not messagebox.askyesno("Konfirmasi", "File asli pada folder Downloads akan dipindahkan ke folder kategori masing-masing. Lanjutkan?"):
                return

        def task():
            organizer = FileOrganizer(self.target_dir)
            success, errors = organizer.organize()
            if success:
                self.history_mgr.add_batch_record(str(self.target_dir), success)
            self.root.after(0, lambda: self.finish_organize(success, errors))

        threading.Thread(target=task, daemon=True).start()

    def finish_organize(self, success, errors):
        msg = f"Berhasil merapikan {len(success)} file."
        if errors:
            msg += f"\nGagal memindahkan {len(errors)} file."
        messagebox.showinfo("Selesai", msg)
        self.scanned_files = []
        self.update_treeview()
        self.refresh_dashboard()

    def create_history_view(self):
        frame = tk.Frame(self.content_frame, bg=self.bg_color)
        tk.Label(frame, text="Riwayat Aktivitas & Undo", font=('Segoe UI', 18, 'bold'), bg=self.bg_color).pack(anchor="w", pady=(0, 10))

        tree_frame = tk.Frame(frame, bg=self.bg_color)
        tree_frame.pack(fill="both", expand=True, pady=10)

        columns = ("id", "timestamp", "target", "total", "status")
        self.hist_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        
        self.hist_tree.heading("id", text="ID Batch")
        self.hist_tree.heading("timestamp", text="Waktu")
        self.hist_tree.heading("target", text="Folder Target")
        self.hist_tree.heading("total", text="Total File")
        self.hist_tree.heading("status", text="Status")

        self.hist_tree.column("id", width=130)
        self.hist_tree.column("timestamp", width=150)
        self.hist_tree.column("target", width=300)
        self.hist_tree.column("total", width=80)
        self.hist_tree.column("status", width=100)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.hist_tree.yview)
        self.hist_tree.configure(yscrollcommand=scrollbar.set)

        self.hist_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btn_frame = tk.Frame(frame, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=10)
        ttk.Button(btn_frame, text="Undo (Kembalikan File Batch Terpilih)", command=self.run_undo_thread, style='Accent.TButton').pack(side="left")

        return frame

    def refresh_history_list(self):
        for row in self.hist_tree.get_children():
            self.hist_tree.delete(row)
        
        history_data = self.history_mgr.get_all_history()
        for item in history_data:
            status = "Sudah di-Undo" if item.get('undone') else "Aktif"
            self.hist_tree.insert("", "end", values=(item['id'], item['timestamp'], item['target_dir'], item['total_files'], status), tags=(item['id'],))

    def run_undo_thread(self):
        selected_item = self.hist_tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih riwayat batch yang ingin di-undo terlebih dahulu.")
            return

        item_values = self.hist_tree.item(selected_item[0], "values")
        batch_id = item_values[0]
        status = item_values[4]

        if status == "Sudah di-Undo":
            messagebox.showinfo("Informasi", "Batch ini sudah pernah di-undo sebelumnya.")
            return

        if not messagebox.askyesno("Konfirmasi Undo", "File akan dikembalikan ke lokasi asalnya. Lanjutkan?"):
            return

        def task():
            history_data = self.history_mgr.get_all_history()
            target_batch = next((h for h in history_data if h['id'] == batch_id), None)
            
            if target_batch:
                success, errors = FileOrganizer.undo_operation(target_batch['operations'])
                if success:
                    self.history_mgr.mark_as_undone(batch_id)
                self.root.after(0, lambda: self.finish_undo(success, errors))

        threading.Thread(target=task, daemon=True).start()

    def finish_undo(self, success, errors):
        msg = f"Berhasil mengembalikan {len(success)} file."
        if errors:
            msg += f"\nGagal mengembalikan {len(errors)} file."
        messagebox.showinfo("Selesai Undo", msg)
        self.refresh_history_list()
        self.refresh_dashboard()

    def create_settings_view(self):
        frame = tk.Frame(self.content_frame, bg=self.bg_color)
        tk.Label(frame, text="Pengaturan Aplikasi", font=('Segoe UI', 18, 'bold'), bg=self.bg_color).pack(anchor="w", pady=(0, 20))

        lbl_target = tk.Label(frame, text="Folder Target Pembersihan:", font=('Segoe UI', 11, 'bold'), bg=self.bg_color)
        lbl_target.pack(anchor="w")

        f_dir = tk.Frame(frame, bg=self.bg_color)
        f_dir.pack(fill="x", pady=5)

        self.ent_folder = ttk.Entry(f_dir, font=('Segoe UI', 10), width=60)
        self.ent_folder.insert(0, str(self.target_dir))
        self.ent_folder.pack(side="left", padx=(0, 10))

        ttk.Button(f_dir, text="Browse...", command=self.browse_folder).pack(side="left")

        self.var_conf = tk.BooleanVar(value=self.settings.get('show_confirmation', True))
        chk_conf = tk.Checkbutton(frame, text="Tampilkan konfirmasi sebelum merapikan file", variable=self.var_conf, bg=self.bg_color, font=('Segoe UI', 10))
        chk_conf.pack(anchor="w", pady=15)

        ttk.Button(frame, text="Simpan Pengaturan", command=self.save_settings, style='Accent.TButton').pack(anchor="w", pady=10)

        return frame

    def browse_folder(self):
        dir_selected = filedialog.askdirectory(initialdir=str(self.target_dir))
        if dir_selected:
            self.ent_folder.delete(0, tk.END)
            self.ent_folder.insert(0, dir_selected)

    def save_settings(self):
        new_dir = self.ent_folder.get()
        if Path(new_dir).exists():
            self.target_dir = Path(new_dir)
            self.settings.set('target_folder', str(self.target_dir))
            self.settings.set('show_confirmation', self.var_conf.get())
            messagebox.showinfo("Berhasil", "Pengaturan berhasil disimpan.")
            self.refresh_dashboard()
        else:
            messagebox.showerror("Error", "Direktori yang dipilih tidak valid atau tidak ditemukan.")

    def create_about_view(self):
        frame = tk.Frame(self.content_frame, bg=self.bg_color)
        tk.Label(frame, text="Tentang Desktop File Sorter", font=('Segoe UI', 18, 'bold'), bg=self.bg_color).pack(anchor="w", pady=(0, 10))
        
        desc = (
            "Desktop File Sorter adalah aplikasi desktop Windows yang dirancang khusus untuk "
            "membantu merapikan folder Downloads Anda secara nyata, aman, dan efisien.\n\n"
            "• Versi: 1.0.0\n"
            "• Teknologi: Python, Tkinter, Pathlib, Shutil\n"
            "• Penyimpanan Metadata: %APPDATA%/DesktopFileSorter/\n\n"
            "Dikembangkan dengan prioritas keamanan data pengguna (tidak menghapus file, "
            "tidak melakukan overwrite, serta menyediakan sistem Undo yang handal)."
        )
        tk.Label(frame, text=desc, font=('Segoe UI', 11), bg=self.bg_color, justify="left").pack(anchor="w", pady=10)

        return frame

    def open_folder_explorer(self):
        import subprocess
        try:
            subprocess.Popen(f'explorer "{self.target_dir}"')
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka folder: {e}")
