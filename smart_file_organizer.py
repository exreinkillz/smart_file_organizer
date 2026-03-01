import os
import shutil
import argparse
import json
import logging

logging.basicConfig(
    filename = "organizer.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

default_extension_map = {
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".pdf": "Documents"
}
default_path = os.path.join(os.path.expanduser("~"), "Downloads")

if not os.path.exists("extension_map.json"):
    print("extension_map.json not found. Creating default one...")
    with open("extension_map.json", "w") as f:
        json.dump(default_extension_map, f, indent=4)

with open("extension_map.json", "r") as f:
    extension_map = json.load(f)

parser = argparse.ArgumentParser(description="A tool to organize your files")
parser.add_argument("--dry-run",
                    action="store_true",
                    help="Show what would happen without moving files")
parser.add_argument("folder_path",
                    nargs = "?",
                    default = default_path,
                    help="Folder to organize files in")
args = parser.parse_args()
folder_path = args.folder_path

if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()
if not os.path.isdir(folder_path):
    print("Folder is not a directory!")
    exit()

files = os.listdir(folder_path)
total_files = len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])
moved_files = 0

for file in files:
    full_path = os.path.join(folder_path, file)
    if not os.path.isfile(full_path):
        continue

    name, ext = os.path.splitext(file)
    category = extension_map.get(ext, "Other")
    category_path = os.path.join(folder_path, category)
    os.makedirs(category_path, exist_ok=True)

    new_name = file
    counter = 1
    while os.path.exists(os.path.join(category_path, new_name)):
        new_name = (f"{name}_{counter}{ext}")
        counter += 1

    destination = os.path.join(category_path, new_name)

    if args.dry_run:
        print("Would move:", file)
        logging.info(f"DRY RUN: {file} → {os.path.join(category_path, new_name)}")
    else:
        shutil.move(full_path, destination)
        moved_files += 1
        print(f"{file} → {os.path.join(category, new_name)}")
        logging.info(f"MOVED: {file} → {os.path.join(category, new_name)}")

print("\n--- Summary ---")
print(f"Total files: {total_files}")
if args.dry_run:
    print("Dry-run mode: No files were moved.")
    logging.info("Dry-run completed: No files were moved.")
else:
    print(f"Files moved: {moved_files}")
    logging.info(f"Files moved: {moved_files}/{total_files}")


