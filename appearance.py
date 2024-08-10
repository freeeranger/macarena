import os
import utils
import logger

def set_dark_mode(status: bool):
    command = f"""
    tell application "System Events"
        set dark mode of appearance preferences to {"true" if status else "false"}
    end tell
    """
    utils.execute_osascript(command)

def set_accent_color(color: str):
    color_map = {
        "red": 0,
        "orange": 1,
        "yellow": 2,
        "green": 3,
        "blue": 4,
        "purple": 5,
        "pink": 6,
        "graphite": -1
    }
    os.system(f"defaults write -g AppleAccentColor -int {str(color_map[color])}")
    os.system("killall Dock")

def set_wallpaper(path: str):
    # TODO somehow fetch the wallpaper as well and store it in correct location, maybe a wallpaper folder as part of the config?
    path = os.path.expanduser(path)

    if not os.path.exists(path):
        logger.log_err(f"{path} does not exist", "appearance.set_wallpaper")
        return
    
    command = f"""
    tell application "Finder"
        set desktop picture to POSIX file "{path}"
    end tell
    """
    utils.execute_osascript(command)