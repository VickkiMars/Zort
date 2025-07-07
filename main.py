from arrange import create_folders, move_files_to_folders
from retrieve_data import Files
from name_clusters import name
from cluster import Cluster
import os

res = []
def flatten(data):

    for ent in data.keys():
        if isinstance(data[ent], dict):
            flatten(data[ent])
        else:
            res.extend(data[ent])
    return res

def run():
    named_dir = {}
    path = input("paste or enter path to folder to be sorted: ")
    pathObj = Files(path).files
    print(pathObj)

    flattened = flatten(pathObj)
    print(flattened)
    print("Sorting files 🎉🎉🎉")
    if os.path.exists(path):
        clusters = Cluster(flattened).clusters
        print(clusters)
        for key, value in clusters:
            new_key = name(value)
            named_dir[new_key] = value
    else:
        print(f"Path {path} does not exist")

    print("Creating new files and folders 🎉🎉🎉")
    for key, value in named_dir:
        if isinstance(value, list):
            create_folders(key)
            move_files_to_folders(key, value)

if __name__ == "__main__":
    run()
        

