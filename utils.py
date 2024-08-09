import os

def execute_osascript(command):
    os.system(f"osascript -e '{command}'")