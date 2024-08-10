import os
from utils import text_bold
from typing import List, Tuple

def set_app_icons(icons: List[Tuple[str, str]]):
    print(text_bold("Applying custom app icons"))

    # Apply icons
    for icon in icons:
        set_app_icon(icon[0], icon[1])
    
    # Clear cache
    os.system("sudo rm -rf /Library/Caches/com.apple.iconservices.store")
    os.system("sudo rm -rf ~/Library/Caches/com.apple.iconservices.store")
    
    print("✅ Cleared icon cache")
    print()
    

def set_app_icon(icon: str, app_path: str):
    os.system(f"sudo cp \"./config/icons/{icon}\" \"{app_path}\"")
    print(f"✅ Applied icon {text_bold(icon)}")
