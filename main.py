import appearance
import trackpad
import dock
import package
import dotfiles
import theming
import other
from utils import text_bold

if package.init():
    package.set_taps(["heroku/brew"])
    package.set_packages([
        "git",
        "gitui",
        "neovim",
        "bat",
        "jq",
        "eza",
        "scc",
        "zoxide",
        "heroku",
        "xclip" # TODO when i remove this line the program should be removed
    ])
    package.set_casks([
        "iterm2", # TODO when i remove this line the program should be removed
        "kitty",
        "firefox@developer-edition",
        "visual-studio-code",
        "steam",
        "font-jetbrains-mono-nerd-font",
        "chatgpt",
        "godot"
    ])

theming.set_app_icons([
    ("kitty.icns", "/Applications/Kitty.app/Contents/Resources/kitty.icns"),
    #("vscode.icns", "/Applications/Visual Studio Code.app/Contents/Resources/Code.icns") # TODO permission issue for this one
])

print(text_bold("Applying settings"))
appearance.set_dark_mode(True)
appearance.set_accent_color("blue")
appearance.set_wallpaper("~/Downloads/wallhaven.png")

trackpad.set_natural_scroll(False)
trackpad.set_secondary_click_mode("bottom_right")

dock.set_tilesize(48)
dock.set_largesize(64)
dock.set_magnification(True)
dock.set_autohide(True)
dock.set_persistent_apps([
    "/Applications/Firefox Developer Edition.app",
    "/Applications/Discord.app",
    "/Applications/Kitty.app",
    "/Applications/Visual Studio Code.app",
])
dock.set_persistent_others([])
dock.set_show_recents(False)
dock.set_show_process_indicators(True)
dock.set_show_progress_indicators(True)
dock.set_orientation("bottom")
print("✅ Done")
print()

dotfiles.set_dotfiles([
    (".zshrc", "~/.zshrc"),
    ("kitty.conf", "~/.config/kitty/kitty.conf")
])

other.create_directories([
    "~/dev",
    "~/dev/games",
    "~/dev/other"
])

other.set_oh_my_zsh(True)