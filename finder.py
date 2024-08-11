import os
import logger
from utils import text_bold

def set_show_hidden_files(status):
    os.system(f"defaults write com.apple.finder AppleShowAllFiles -bool {"true" if status else "false"}")


def set_show_breadcrumb(status):
    os.system(f"defaults write com.apple.finder ShowPathbar -bool {"true" if status else "false"}")


def set_show_item_info(status):
    os.system(f"defaults write com.apple.finder ShowStatusBar -bool {"true" if status else "false"}")


def set_show_all_extensions(status):
    os.system(f"defaults write com.apple.finder AppleShowAllExtensions -bool {"true" if status else "false"}")    


def set_preferred_view_size(view_size):
    view_map = {
        "list": "Nlsv",
        "column": "clmv",
        "icon": "icnv"
    }
    
    if view_size not in view_map:
        logger.log_err(
            f"No such view size {text_bold(view_size)}, valid options are: {text_bold("list")}, {text_bold("column")}, {text_bold("icon")}", 
            "finder.set_preferred_view_size"
        )

    os.system(f"defaults write com.apple.finder FXPreferredViewSize -string \"{view_map[view_size]}\"")


def apply():
    os.system("killall Finder")