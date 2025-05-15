"""
📄 Project 12: File Search Tool (GUI)
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today’s date]

🧠 Description:
This GUI-based Python tool allows users to search for files inside any selected folder by filename or keyword.
It displays all matched file paths and allows the user to open their location with a single click.

📦 Features:
- Browse and select any directory
- Enter a keyword or partial filename
- Display all matching files (recursively)
- Open the containing folder with one click

🧰 Tools & Modules Used:
- tkinter: for GUI
- os: for file searching
- subprocess: to open folder (Windows)

💡 How to Use:
1. Run the script
2. Select a folder
3. Enter a keyword (e.g., "report")
4. Click 'Search'
5. Click on any result to open its folder

"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def browse_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def search_files():
    folder = folder_path.get()
    keyword = keyword_entry.get().lower()
    results_list.delete(0, tk.END)

    if not folder or not keyword:
        messagebox.showerror("Input Error", "Please select a folder and enter a keyword.")
        return

    matches = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if keyword in file.lower():
                full_path = os.path.join(root, file)
                matches.append(full_path)

    if not matches:
        results_list.insert(tk.END, "No files found.")
    else:
        for match in matches:
            results_list.insert(tk.END, match)

def open_selected_folder(event):
    selection = results_list.curselection()
    if selection:
        file_path = results_list.get(selection[0])
        folder = os.path.dirname(file_path)
        subprocess.Popen(f'explorer "{folder}"')

# GUI Setup
root = tk.Tk()
root.title("File Search Tool")
root.geometry("600x400")

folder_path = tk.StringVar()

tk.Label(root, text="Select Folder:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=60).pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

tk.Label(root, text="Enter filename keyword:").pack(pady=5)
keyword_entry = tk.Entry(root, width=40)
keyword_entry.pack(pady=5)

tk.Button(root, text="Search", command=search_files).pack(pady=10)

results_list = tk.Listbox(root, width=80, height=12)
results_list.pack(pady=10)
results_list.bind("<Double-Button-1>", open_selected_folder)

root.mainloop()
