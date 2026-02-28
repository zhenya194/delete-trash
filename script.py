import shutil
from pathlib import Path

delete_folders:list = ["__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".ipynb_checkpoints"]
delete_files:list = [".pyc", ".coverage"]

confirm = input("Confirm launch of script? [Y/N]: ")
if confirm.lower() != "y":
    exit()

for item in Path(".").rglob("*"):
    if item.is_dir() and item.name in delete_folders:
        print(f"Deleting folder {item} ...")
        shutil.rmtree(item, ignore_errors=True)

    elif item.is_file() and (item.suffix in delete_files or item.name == ".coverage"):
        if item.exists():
            print(f"Deleting file: {item}")
            item.unlink(missing_ok=True)

print("Completed.")
