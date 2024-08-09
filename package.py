import os
import subprocess
import logger
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
    for package in packages:
        install_package(package)

def set_casks(casks: List[str]):
    for cask in casks:
        install_cask(cask)

def install_package(name: str):
    res = subprocess.run(["brew", "list", "--formula"], capture_output=True, text=True)
    entries = res.stdout.split("\n")

    for entry in entries:
        if entry == name:
            logger.log_info(f"Package {name} already installed")
            return

    logger.log_info(f"Installing package {name}")
    subprocess.run(["brew", "install", name], capture_output=True, text=True)
    logger.log_info(f"Package {name} installed")

def install_cask(name: str):
    res = subprocess.run(["brew", "list", "--cask"], capture_output=True, text=True)
    entries = res.stdout.split("\n")

    for entry in entries:
        if entry == name:
            logger.log_info(f"Cask {name} already installed")
            return

    logger.log_info(f"Installing cask {name}")
    subprocess.run(["brew", "install", "--cask", name], capture_output=True, text=True)
    logger.log_info(f"Cask {name} installed")