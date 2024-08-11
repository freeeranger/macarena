import os

def set_natural_scroll(status):
    os.system(f"defaults write NSGlobalDomain com.apple.swipescrolldirection -bool {"true" if status else "false"}")

def set_secondary_click_mode(mode):
    if mode == "bottom_right": # TODO MIGHT not be working?? gotta check
        os.system("defaults write com.apple.AppleMultitouchTrackpad TrackpadCornerSecondaryClick -int 2")
        os.system("defaults write com.apple.AppleMultitouchTrackpad TrackpadRightClick -int 0")
        os.system("killall SystemUIServer")