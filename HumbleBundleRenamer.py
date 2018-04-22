import os
import shutil

origin_dir = "L:\Downloads\HumbleBundle"
destination_dir = "L:\Downloads\To Move to DrivePool"

for path, directories, files in os.walk(origin_dir):
    if path.endswith("ebook"):
        folder_name = os.path.normpath(path).split(os.sep)[-2]
        move_folder_name = os.path.join(destination_dir, "Books", folder_name)
        print(" ".join(["Moving", path, "to", move_folder_name]))
        shutil.move(path, move_folder_name)
    elif path.endswith("audio"):
        folder_name = os.path.normpath(path).split(os.sep)[-2]
        move_folder_name = os.path.join(destination_dir, "Audio", folder_name)
        print(" ".join(["Moving", path, "to", move_folder_name]))
        shutil.move(path, move_folder_name)
    elif path.endswith("android") or path.endswith("linux") or path.endswith("mac") or path.endswith("windows"):
        folder_name = os.path.normpath(path).split(os.sep)[-2]
        move_folder_name = os.path.join(destination_dir, "Game", folder_name)
        print(" ".join(["Moving", os.path.join(path, ".."), "to", move_folder_name]))
        shutil.move(os.path.join(path, ".."), move_folder_name)
    if not os.listdir(path):
        print(" ".join(["Removing", path]))
        os.rmdir(path)

for path, directories, files in os.walk(destination_dir):
    if not os.listdir(path):
        print(" ".join(["Removing", path]))
        os.rmdir(path)
    elif path.endswith("ebook"):
        folder_name = os.path.normpath(path).split(os.sep)[-2]
        move_folder_name = os.path.join(destination_dir, "Books", folder_name)
        for each_file in files:
            print(" ".join(["Moving", os.path.join(path, each_file), "to", os.path.join(move_folder_name, each_file)]))
            shutil.move(os.path.join(path, each_file), os.path.join(move_folder_name, each_file))
    elif path.endswith("audio"):
        folder_name = os.path.normpath(path).split(os.sep)[-2]
        move_folder_name = os.path.join(destination_dir, "Audio", folder_name)
        for each_file in files:
            print(" ".join(["Moving", os.path.join(path, each_file), "to", os.path.join(move_folder_name, each_file)]))
            shutil.move(os.path.join(path, each_file), os.path.join(move_folder_name, each_file))
    if os.path.normpath(path).split(os.sep)[-2] != "Comics":
        try:
            for each_file in files:
                if each_file.endswith('.cbz'):
                    folder_name = os.path.normpath(path).split(os.sep)[-1]
                    move_folder_name = os.path.join(destination_dir, "Comics", folder_name)
                    print("Moving " + path + " to " + move_folder_name)
                    shutil.move(path, move_folder_name)
                    continue
        except (WindowsError, IOError):
            continue
