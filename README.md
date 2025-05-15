# 🗂️ Project 12: File Search Tool (GUI)

**👨‍💻 Created by:** Hashir Adnan  
🌐 [www.techthf.xyz](https://www.techthf.xyz)  
🗓️ May 14, 2025

---

## 🧠 Description

This is a **GUI-based file search utility** made with Python.  
It allows users to **search for files** inside any selected folder (recursively) based on filename or keyword.  
Results are listed in a clickable list — double-clicking any result opens its containing folder in File Explorer (Windows only).

---

## 📦 Features

- 📁 Browse and select any directory
- 🔍 Search files by name or keyword (case-insensitive)
- 🗂️ Recursively scans subfolders
- 🖱️ Double-click result to open its folder
- 🧼 Clean and responsive UI

---

## 🧰 Tools & Modules Used

- [`tkinter`](https://docs.python.org/3/library/tkinter.html): for building the GUI  
- [`os`](https://docs.python.org/3/library/os.html): for file traversal  
- [`subprocess`](https://docs.python.org/3/library/subprocess.html): to open folders (Windows only)

---

## 💡 How to Use

1. Run the script:
   ```bash
   python main.py
