import os
import shutil
from utils import text_bold
import logger
from pathlib import Path

def set_dotfiles(dotfiles):
    print(text_bold("Syncing dotfiles"))

    for dotfile in dotfiles:
        add_dotfile(dotfile["source"], dotfile["target"])

    print()

def add_dotfile(name: str, final_dest: str):
    source_path = f"./config/dotfiles/{name}"

    path = Path(source_path)

    if not path.exists():
        logger.log_err(f"Dotfile path {text_bold(name)} doesn't exist", "dotfiles.set_dotfiles")
        return

    if path.is_file():
        dest_file = os.path.expanduser(final_dest)

        shutil.copy(source_path, dest_file)
        print(f"✅ Synced dotfile {text_bold(name)}")
        return
    
    if path.is_dir():
        dest_dir = os.path.expanduser(final_dest)

        shutil.copytree(source_path, dest_dir, dirs_exist_ok=True)
        print(f"✅ Synced dotfile directory {text_bold(name)}")    