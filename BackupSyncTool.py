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
        self.root.geometry("600x250")

        # Main Frame for Layout
        main_frame = tk.Frame(root)
        main_frame.pack(pady=10)

        # === Primary Drive (Left Side) ===
        primary_frame = tk.Frame(main_frame)
        primary_frame.grid(row=0, column=0, padx=10)

        tk.Label(primary_frame, text="Primary Drive (Source):", font=("Arial", 12)).pack()
        self.primary_path_var = tk.StringVar()
        self.primary_entry = tk.Entry(primary_frame, textvariable=self.primary_path_var, width=30, state="readonly")
        self.primary_entry.pack(pady=5)

        tk.Button(primary_frame, text="Browse", command=self.select_primary).pack()

        # === Middle Separator (|) ===
        separator = tk.Label(main_frame, text=" | ", font=("Arial", 16, "bold"))
        separator.grid(row=0, column=1, padx=10)

        # === Backup Drive (Right Side) ===
        backup_frame = tk.Frame(main_frame)
        backup_frame.grid(row=0, column=2, padx=10)

        tk.Label(backup_frame, text="Backup Drive (Destination):", font=("Arial", 12)).pack()
        self.backup_path_var = tk.StringVar()
        self.backup_entry = tk.Entry(backup_frame, textvariable=self.backup_path_var, width=30, state="readonly")
        self.backup_entry.pack(pady=5)

        tk.Button(backup_frame, text="Browse", command=self.select_backup).pack()

        # === Sync Button & Status ===
        self.sync_btn = tk.Button(root, text="Sync Now", command=self.start_sync, bg="green", fg="white", font=("Arial", 12))
        self.sync_btn.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 10), fg="blue")
        self.status_label.pack()

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

        self.status_label.config(text="Syncing...", fg="orange")
        self.root.update_idletasks()

        # Run sync in a separate thread to avoid UI freezing
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

            self.status_label.config(text=f"Sync Completed Successfully ✅ ({copied_files} new files copied)", fg="green")
        except Exception as e:
            self.status_label.config(text="Sync Failed ❌", fg="red")
            messagebox.showerror("Error", f"Sync failed: {str(e)}")

# 🚀 Launch Application
if __name__ == "__main__":
    root = tk.Tk()
    app = BackupSyncApp(root)
    root.mainloop()
