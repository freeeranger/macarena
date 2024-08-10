import os
import shutil
from utils import text_bold
from typing import List, Tuple
import logger

def set_dotfiles(dotfiles: List[Tuple[str, str]]):
    print(text_bold("Syncing dotfiles"))

    for dotfile in dotfiles:
        add_dotfile(dotfile[0], dotfile[1])

    print()

def add_dotfile(name: str, final_dest: str):
    source_file = f"./config/dotfiles/{name}"

    if not os.path.exists(source_file):
        logger.log_err(f"Dotfile {text_bold(name)} doesn't exist", "dotfiles.set_dotfiles")
        return

    dest_file = os.path.expanduser(final_dest)

    shutil.copy(source_file, dest_file)
    print(f"✅ Synced dotfile {text_bold(name)}")