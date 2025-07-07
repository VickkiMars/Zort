import os

class Files():
    def __init__(self, root_dir=""):
        self.root_dir = root_dir
        print(f"\nSearching [{root_dir}] 🎉🎉🎉\n")
        self.files  = self.moonWalk()

    def moonWalk(self, path=""):
        if path == "":
            path = self.root_dir
        tree = {}
        tree["%**_"] = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                tree[entry] = self.moonWalk(full_path)  # recurse into subdirectory
            else:
                tree["%**_"].append(entry)  # file: no further nesting
        return tree

                
if __name__ == "__main__":
    filepath = r"C:\Users\Victor\Desktop\testdir"
    ins = Files(filepath)
    print(ins.files)


