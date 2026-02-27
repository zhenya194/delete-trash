import os
import shutil

delete_this_folders:list[str] = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".ipynb_checkpoints",
]

is_confirmed:str = input("Confirm launch of script? [Y/N]")
if is_confirmed != "Y" or is_confirmed != "y":
    exit()

for main, folders, files in os.walk("."):
    for folder in folders:
        if folder in delete_this_folders:
            path = os.path.join(main, folder)
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

    for file in files:
        if file.endswith(".pyc"):
            path = os.path.join(main, file)
            print(f"Deleting {path} ...")
            os.remove(path)
        elif file.endswith(".coverage"):
            path = os.path.join(main, folder)
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

print("Completed.")
