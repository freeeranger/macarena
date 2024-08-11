import os
from utils import text_bold

def create_directories(directories):
    print(text_bold("Creating directories"))
    for dir in directories:
        dir_expanded = os.path.expanduser(dir)

        if os.path.exists(dir_expanded):
            continue

        os.makedirs(dir_expanded, exist_ok=True)
        print(f"✅ Created directory {dir}")
    print()


def set_oh_my_zsh(status):
    if os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
        if not status:
            os.system("uninstall_oh_my_zsh")
        return

    if not status:
        return

    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')