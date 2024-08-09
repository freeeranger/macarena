import os
import utils

def set_dark_mode(status):
    command = f"""
    tell application "System Events"
        set dark mode of appearance preferences to {"true" if status else "false"}
    end tell
    """
    utils.execute_osascript(command)

def set_accent_color(color):
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
