from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from main import scanning, Organize


selected_folder = ""

def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()

    if selected_folder:
        folder_label.config(text=f"📂 {selected_folder}")

def organize_files():
    if not selected_folder:
        status.config(text="Status: Please select a folder first ❌")
        return

    status.config(text="Status: Organizing files... ⏳")
    root.update_idletasks()

    files =  scanning(selected_folder)
    Organize(selected_folder,files)

    status.config(text="Status: Done ✅")



root = tk.Tk()
root.title("File Organizer")
root.geometry("420x320")
root.resizable(False, False)

# background color
root.configure(bg="#f5f7fa")

# title
folder_label = tk.Label(
    root,
    text="No folder selected",
    font=("Segoe UI", 10),
    bg="#f5f7fa",
    fg="#34495e",
    wraplength=380,
    justify="center"
)
folder_label.pack(pady=10)

title = tk.Label(
    root,
    text="File Organizer",
    font=("Segoe UI", 18, "bold"),
    bg="#f5f7fa",
    fg="#2c3e50"
)
title.pack(pady=20)
style = ttk.Style()
style.theme_use("default")

style.configure(
    "TButton",
    font=("Segoe UI", 11),
    padding=10
)

select_btn = ttk.Button(root, text="Select Folder", command=select_folder)
select_btn.pack(pady=10)

organize_btn = ttk.Button(
    root,
    text="✨ Organize Files",
    command=organize_files
)
organize_btn.pack(pady=10)

status = tk.Label(
    root,
    text="Status: Ready",
    font=("Segoe UI", 10),
    bg="#f5f7fa",
    fg="#7f8c8d"
)
status.pack(pady=20)



root.mainloop()
