import appearance
import trackpad
import dock
import package
import dotfiles
import defaults
from utils import text_bold

if package.init():
    package.set_packages([
        "git",
        "gitui",
        "neovim",
        "bat",
        "jq",
        "eza",
        "scc"
    ])
    package.set_casks([
        "iterm2",
        "firefox@developer-edition",
        "visual-studio-code",
        "steam",
        "font-jetbrains-mono-nerd-font"
    ])

print(text_bold("Applying settings"))
appearance.set_dark_mode(True)
appearance.set_accent_color("blue")
appearance.set_wallpaper("~/Downloads/wallhaven.png")

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

dotfiles.set_dotfiles([
    (".zshrc", "~/.zshrc"),
])

# TODO FIX: defaults.set_default("com.googlecode.iterm2", '"Normal Font" -string "JetBrainsMono Nerd Font 14"')