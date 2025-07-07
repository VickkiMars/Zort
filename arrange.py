import os
import shutil

def create_folders(folder_names):
    """
    Create folders if they do not already exist.

    Parameters:
    - folder_names (list): A list of folder names (str) to create in the current working directory.
    """
    for folder in folder_names:
        if not os.path.exists(folder):
            print(f"Creating folder: {folder} 🎉🎉🎉")
            os.makedirs(folder)
        else:
            print(f"Folder already exists: {folder}")


def move_files_to_folders(folder_name, file_names):
    """
    Move a list of files into the specified folder.

    Parameters:
    - folder_name (str): The name of the folder to move files into.
    - file_names (list): A list of filenames (str) to move.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")

    for file in file_names:
        if os.path.exists(file):
            dest = os.path.join(folder_name, os.path.basename(file))
            shutil.move(file, dest)
            print(f"Moved {file} to {folder_name}")
        else:
            print(f"File not found: {file}")
