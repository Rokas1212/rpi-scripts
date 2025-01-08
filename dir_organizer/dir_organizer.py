#!/usr/bin/env python3
"""
Directory organizer script
Date created: 2025-01-08
Date updated: 2025-01-08
Creator: Rokas Čiuplinskas
"""

import os
import shutil
import argparse

def parse_arguments():
        parser = argparse.ArgumentParser(description="Organize files in a directory.")
        parser.add_argument("--source", required=True, help="Source directory that needs to be organized")
        return parser.parse_args()

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

def check_existance(item_path, target_dir):
    target_path = os.path.join(target_dir, item_path.split('/')[-1])
    return os.path.exists(target_path)

def move_files(categorized_files, source):
    confirmation = input("Press Enter To Continue...")
    if confirmation != "":
        print("Aborting")
        return
    try:
        for category, items in categorized_files.items():
            target_dir = os.path.join(source,category)
            if len(items) < 1:
                continue
            os.makedirs(target_dir, exist_ok=True)
            for item in items:
                if check_existance(item, target_dir):
                    print(f"{os.path.join(target_dir, item.split('/')[-1])} already exists, skipping...")
                    continue
                shutil.move(item, target_dir)
                print(f"Moved {item.split('/')[-1]} to:{target_dir}")
    except Exception as e:
        print(f"An error occured while moving files: {e}")

if __name__ == "__main__":
    args = parse_arguments()

    source_dir = args.source

    files_list = []

    scan_dir(source_dir, files_list)

    categorized_files = categorize_files(files_list)

    move_files(categorized_files, source_dir)
