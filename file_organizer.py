import os
import shutil

path = input("Input folder destination: ") 
items = os.listdir(path)

folders = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".tiff": "Images",
    ".webp": "Images",
    ".avif": "Images",
    ".svg": "Images",
    ".jfif": "Images",
    ".JPG": "Images",
    ".doc": "Document",
    ".docx": "Document",
    ".pdf": "Document",
    ".txt": "Document",
    ".xlsx": "Document",
    ".xls": "Document",
    ".pdf": "Pdf",
    ".mp4": "Video",
    ".m4v": "Video",
    ".mov": "Video",
    ".mkv": "Video",
    ".exe": "Application",
    ".zip": "Zip",
    ".7z": "Zip",
    ".rar": "Zip",
    ".tar": "Zip",
    ".ppt": "Presentation",
    ".pptx": "Presentation",
    ".ppsx": "Presentation",

}

for folder in folders:
    full_folder = os.path.join(path, folders[folder])
    os.makedirs(full_folder, exist_ok=True)
    for file in items:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            name,ext = os.path.splitext(file)
            if ext == (folder):
                shutil.move(full_path,full_folder)
