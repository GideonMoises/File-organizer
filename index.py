import os
import shutil

path = r"C:\Users\carbo\Downloads" 

items = os.listdir(path)

folders = ["folderImg", "folderDoc", "folderZip", "folderVid"]

for folder in folders:
    full_folder = os.path.join(path, folder)
    os.makedirs(full_folder, exist_ok=True)

for file in items:
    full_path = os.path.join(path, file) 
    if os.path.isfile(full_path):
        name, ext = os.path.splitext(file)
        print(ext)
        if ext == ".png" or ext == ".jpeg" or ext == ".JPG" or ext == ".jfif" or ext == ".jpg":
            shutil.move(full_path, os.path.join(path, folders[0]))
        elif ext == ".docx" or ext == ".doc" or ext == ".pdf":
             shutil.move(full_path, os.path.join(path, folders[1]))
        elif ext == ".zip" or ext == ".7z" or ext == ".rar":
            shutil.move(full_path, os.path.join(path, folders[2]))
        elif ext == ".mp4":
            shutil.move(full_path, os.path.join(path, folders[2]))
