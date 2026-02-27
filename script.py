import os
import shutil

delete_this_folders:list[str] = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".ipynb_checkpoints",
]

for root, folders, files in os.walk("."):
    for folder in folders:
        if folder in delete_this_folders:
            path = os.path.join(root, folder)
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

    for file in files:
        if file.endswith(".pyc"):
            path = os.path.join(root, file)
            print(f"Deleting {path} ...")
            os.remove(path)
        elif file.endswith(".coverage"):
            path = os.path.join(root, folder)
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

print("Completed.")
