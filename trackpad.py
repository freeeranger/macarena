import os

def set_natural_scroll(status):
    os.system(f"defaults write NSGlobalDomain com.apple.swipescrolldirection -bool {"true" if status else "false"}")
