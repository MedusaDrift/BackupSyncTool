import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

# 🖥️ GUI Backup Sync Utility
class BackupSyncApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Backup Sync Utility")
        self.root.geometry("500x300")

        # Primary Drive Selection
        self.primary_label = tk.Label(root, text="Select Primary Drive (Source):", font=("Arial", 12))
        self.primary_label.pack(pady=5)

        self.primary_path_var = tk.StringVar()
        self.primary_entry = tk.Entry(root, textvariable=self.primary_path_var, width=50, state="readonly")
        self.primary_entry.pack(pady=5)

        self.primary_btn = tk.Button(root, text="Browse", command=self.select_primary)
        self.primary_btn.pack(pady=5)

        # Backup Drive Selection
        self.backup_label = tk.Label(root, text="Select Backup Drive (Destination):", font=("Arial", 12))
        self.backup_label.pack(pady=5)

        self.backup_path_var = tk.StringVar()
        self.backup_entry = tk.Entry(root, textvariable=self.backup_path_var, width=50, state="readonly")
        self.backup_entry.pack(pady=5)

        self.backup_btn = tk.Button(root, text="Browse", command=self.select_backup)
        self.backup_btn.pack(pady=5)

        # Sync Button
        self.sync_btn = tk.Button(root, text="Sync Now", command=self.start_sync, bg="green", fg="white")
        self.sync_btn.pack(pady=20)

    def select_primary(self):
        path = filedialog.askdirectory(title="Select Primary Drive (Source)")
        if path:
            self.primary_path_var.set(path)

    def select_backup(self):
        path = filedialog.askdirectory(title="Select Backup Drive (Destination)")
        if path:
            self.backup_path_var.set(path)

    def start_sync(self):
        primary_path = self.primary_path_var.get()
        backup_path = self.backup_path_var.get()

        if not primary_path or not backup_path:
            messagebox.showerror("Error", "Please select both Primary and Backup drives!")
            return

        threading.Thread(target=self.sync_files, args=(primary_path, backup_path), daemon=True).start()

    def sync_files(self, primary, backup):
        copied_files = 0
        try:
            for root_dir, _, files in os.walk(primary):
                relative_path = os.path.relpath(root_dir, primary)
                backup_dir = os.path.join(backup, relative_path)

                if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)

                for file in files:
                    src_file = os.path.join(root_dir, file)
                    dst_file = os.path.join(backup_dir, file)

                    if not os.path.exists(dst_file):
                        shutil.copy2(src_file, dst_file)
                        copied_files += 1

            messagebox.showinfo("Success", f"Sync completed! {copied_files} new files copied.")
        except Exception as e:
            messagebox.showerror("Error", f"Sync failed: {str(e)}")

# 🚀 Launch Application
if __name__ == "__main__":
    root = tk.Tk()
    app = BackupSyncApp(root)
    root.mainloop()

