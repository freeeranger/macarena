import appearance
import trackpad
import dock
import package
from utils import text_bold

if package.init():
    package.set_packages([
        "git",
        "gitui",
        "neovim"
    ])
    package.set_casks([
        "iterm2",
        "firefox@developer-edition",
        "visual-studio-code",
    ])

print(text_bold("Applying settings"))
appearance.set_dark_mode(True)
appearance.set_accent_color("blue")

trackpad.set_natural_scroll(False)

dock.set_tilesize(48)
dock.set_largesize(64)
dock.set_magnification(True)
dock.set_autohide(True)
dock.set_persistent_apps([
    "/Applications/Firefox Developer Edition.app",
    "/Applications/Discord.app",
    "/Applications/Iterm.app",
    "/Applications/Visual Studio Code.app",
])
dock.set_persistent_others([])
dock.set_show_recents(False)
dock.set_show_process_indicators(True)
dock.set_show_progress_indicators(True)
dock.set_orientation("bottom")