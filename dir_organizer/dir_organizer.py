#!/usr/bin/env python3
"""
Directory organizer script
Date created: 2025-01-08
Date updated: 2025-01-08
Creator: Rokas Čiuplinskas
"""

import os
import shutil

def scan_dir(dir, files_list):
    for root, dirs, files in os.walk(dir):
        dirs.clear()
        for file in files:
            files_list.append(os.path.join(root, file))
            print(f"Found {os.path.join(root, file)}")

def categorize_files(files):
    categories = {
            "Documents": [".docx", ".txt", ".pdf", ".pptx", ".doc"],
            "Sheets": [".xlsx", ".csv"],
            "Installers": [".pkg", ".dmg"],
            "Images": [".jpg", ".png", ".gif", ".jpeg", ".svg"],
            "Videos": [".mp4", ".avi", ".mov"],
            "Code": [".py", ".ipynb", ".cpp", ".c", ".cs", ".js", ".jsx", ".ts", ".tsx", ".java", ".class"],
            "Archives": [".zip", ".7z", ".rar", ".tar.gz", ".tgz"]
    }
    
    categorized_dict = {category: [] for category in categories}
    categorized_dict["Uncategorized"] = []
    
    
    for file in files:
        categorized = False
        for category, extensions in categories.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                categorized_dict[category].append(file)
                categorized = True
                break
        if not categorized:
            categorized_dict["Uncategorized"].append(file)
    return categorized_dict

def move_files(categorized_files, source):
    confirmation = input("Press Enter To Continue...")
    if confirmation != "":
        print("Aborting")
        return
    for category, items in categorized_files.items():
        target_dir = os.path.join(source,category)
        os.makedirs(target_dir, exist_ok=True)
        for item in items:
            shutil.move(item, target_dir)
            print(f"Moved {item} to:\n{target_dir}")

if __name__ == "__main__":
    print("""
    ------------------------------------------------------------
    |   Directories will be organized within 1 level of depth  |
    |   Subdirectories will stay untouched                     |
    ------------------------------------------------------------
    """)
    source_dir = input("Enter the directory to organize: ")
    files_list = []
    scan_dir(source_dir, files_list)
    categorized_files = categorize_files(files_list)
    move_files(categorized_files, source_dir)
