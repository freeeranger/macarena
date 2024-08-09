import os
import subprocess
import logger
from utils import text_bold
from typing import List


def init() -> bool:
    try:
        subprocess.run(["brew", "--version"], capture_output=True)
    except:
        # Install homebrew
        logger.log_info("Homebrew not found, installing...")
        #os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        logger.log_info("Homebrew installed")

        # Add brew to path
        zprofile_path = os.path.expanduser("~/.zprofile")
        with open(zprofile_path, "a") as file:
            file.write("\n")
            file.write('eval "$(/opt/homebrew/bin/brew shellenv)"')
        os.system(f"source {zprofile_path}")

        logger.log_info("Homebrew installed, please restart your terminal before running any other commands")
        return False
    
    return True


def set_packages(packages: List[str]):
    print(text_bold("Verifying packages"))
    for package in packages:
        install_package(package)
    print()


def set_casks(casks: List[str]):
    print(text_bold("Verifying casks"))
    for cask in casks:
        install_cask(cask)
    print()

def install_package(name: str):
    # check if package exists
    res = subprocess.run(["brew", "info", name], capture_output=True, text=True)
    if res.stdout == "":
        print(f"⚠️ Package {text_bold(name)} doesn't exist")
        return

    # check if package is installed
    res = subprocess.run(["brew", "list", "--formula"], capture_output=True, text=True)
    entries = res.stdout.split("\n")
    for entry in entries:
        if entry == name:
            print(f"✅ Package {text_bold(name)} already installed")
            return

    # install package
    print(f"Installing package {text_bold(name)}")
    subprocess.run(["brew", "install", name], capture_output=True, text=True)
    print(f"✅ Package {text_bold(name)} installed")


def install_cask(name: str):
    # check if cask exists
    res = subprocess.run(["brew", "info", "--cask", name], capture_output=True, text=True)
    if res.stdout == "":
        print(f"⚠️ Cask {text_bold(name)} doesn't exist")
        return
    
    # check if cask is installed
    res = subprocess.run(["brew", "list", "--cask"], capture_output=True, text=True)
    entries = res.stdout.split("\n")
    for entry in entries:
        if entry == name:
            print(f"✅ Cask {text_bold(name)} already installed")
            return

    # install cask
    print(f"Installing cask {text_bold(name)}")
    subprocess.run(["brew", "install", "--cask", name], capture_output=True, text=True)
    print(f"✅ Cask {text_bold(name)} installed")