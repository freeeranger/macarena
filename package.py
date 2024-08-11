import os
import subprocess
import logger
from utils import text_bold


def init() -> bool:
    try:
        subprocess.run(["brew", "--version"], capture_output=True)
    except:
        # Install homebrew
        logger.log_info("Homebrew not found, installing...")
        os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
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


def set_taps(taps):
    for tap in taps:
        os.system(f"brew tap {tap}")


def set_packages(packages):
    print(text_bold("Verifying packages"))

    installed_packages = subprocess.run(["brew", "list", "--formula"], capture_output=True, text=True).stdout.split("\n")

    for package in packages:
        if package in installed_packages:
            print(f"✅ Package {text_bold(package)} already installed")
            continue
        
        if subprocess.run(["brew", "info", package], capture_output=True, text=True).stdout == "":
            print(f"⚠️ Package {text_bold(package)} doesn't exist")
            continue

        install_package(package)

    print()


def set_casks(casks):
    print(text_bold("Verifying casks"))

    installed_casks = subprocess.run(["brew", "list", "--cask"], capture_output=True, text=True).stdout.split("\n")

    for cask in casks:
        if cask in installed_casks:
            print(f"✅ Cask {text_bold(cask)} already installed")
            continue
            
        if subprocess.run(["brew", "info", "--cask", cask], capture_output=True, text=True).stdout == "":
            print(f"⚠️ Cask {text_bold(cask)} doesn't exist")
            continue

        install_cask(cask)

    print()


def install_package(name):
    first_msg = f"Installing package {text_bold(name)}..."
    print(first_msg)
    
    subprocess.run(["brew", "install", name], capture_output=True, text=True)

    second_msg = f"✅ Package {text_bold(name)} installed"
    print("\033[F" + second_msg + " " * max(len(first_msg) - len(second_msg), 0))


def install_cask(name):
    first_msg = f"Installing cask {text_bold(name)}..."
    print(first_msg)
    
    subprocess.run(["brew", "install", "--cask", name], capture_output=True, text=True)

    second_msg = f"✅ Cask {text_bold(name)} installed"
    print("\033[F" + second_msg + " " * max(len(first_msg) - len(second_msg), 0))
