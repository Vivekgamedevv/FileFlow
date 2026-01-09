import os
import shutil

mapping = {
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "mp3": "Music",
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "docx": "Documents",
    "xlsx": "Documents",
    "pdf": "Documents",
    "txt": "Documents",
    "rar": "Archive",
    "zip": "Archive",
    "7z": "Archive",
    "py": "Code",
    "c": "Code",
    "java": "Code",
    "html": "Code"
}


def scanning(root_dir):
    files = []
    items = os.listdir(root_dir)
    print("SCAN START")

    for a in items:
        value = os.path.isfile(root_dir + "/" + a)
        if value == True:
            files.append(a)

    print("SCAN END")

    return files


# LOOP FOR JUST CHECKING WHETHER IT IS A FILE OR FOLDER
def Organize(root_dir,files):
    os.makedirs(root_dir + "/Organized_Folders", exist_ok=True)

    final_dir = root_dir + "/Organized_Folders"
    junk_dir = final_dir + "/Junk"

    for x in files:
        if '.' in x:
            ext = x.rsplit('.', 1)
            search = mapping.get(ext[1].lower(), "Junk")
            dir_val = os.path.isdir(final_dir + "/" + search)

            if dir_val == True:
                shutil.move(root_dir + "/" + x, final_dir + "/" + search)
            else:
                os.makedirs(final_dir + "/" + search, exist_ok=True)
                shutil.move(root_dir + "/" + x, final_dir + "/" + search)

        else:
            dir_val = os.path.isdir(junk_dir)

            if dir_val == True:
                shutil.move(root_dir + "/" + x, junk_dir)
            else:
                os.makedirs(junk_dir, exist_ok=True)
                shutil.move(root_dir + "/" + x, junk_dir)
