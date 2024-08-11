import appearance
import trackpad
import dock
import package
import dotfiles
import theming
import other
from utils import text_bold
import finder

import config

if not package.init():
    exit()


config.init()

package.set_taps(config.get_option(["package", "taps"]))
# TODO when i remove xclip / iterm2 from below they should actually be removed from the system too
package.set_packages(config.get_option(["package", "packages"]))
package.set_casks(config.get_option(["package", "casks"]))


# TODO this should use the same method as dropping icon in info window to work on all apps
# theming.set_app_icons([
#    ("kitty.icns", "/Applications/Kitty.app/Contents/Resources/kitty.icns"),
#    #("vscode.icns", "/Applications/Visual Studio Code.app/Contents/Resources/Code.icns") # perm issue on this one
# ])


print(text_bold("Applying settings"))
appearance.set_dark_mode(config.get_option(["appearance", "dark_mode"]))
appearance.set_accent_color(config.get_option(["appearance", "accent_color"]))

wallpaper_path = config.get_option(["appearance", "wallpaper"])
if wallpaper_path != "":
    appearance.set_wallpaper(wallpaper_path)

trackpad.set_natural_scroll(config.get_option(["trackpad", "natural_scroll"]))
trackpad.set_secondary_click_mode(config.get_option(["trackpad", "secondary_click_mode"]))

dock.set_tilesize(config.get_option(["dock", "tilesize"]))
dock.set_largesize(config.get_option(["dock", "largesize"]))
dock.set_magnification(config.get_option(["dock", "magnification"]))
dock.set_autohide(config.get_option(["dock", "autohide"]))
dock.set_persistent_apps(config.get_option(["dock", "persistent_apps"]))
dock.set_persistent_others(config.get_option(["dock", "persistent_others"]))
dock.set_show_recents(config.get_option(["dock", "show_recents"]))
dock.set_show_process_indicators(config.get_option(["dock", "show_process_indicators"]))
dock.set_show_progress_indicators(config.get_option(["dock", "show_progress_indicators"]))
dock.set_orientation(config.get_option(["dock", "orientation"]))
print("✅ Done")
print()

dotfiles.set_dotfiles(config.get_option(["dotfiles", "dotfiles"]))

other.create_directories(config.get_option(["other", "create_directories"]))
other.set_oh_my_zsh(config.get_option(["other", "oh_my_zsh"]))

finder.set_show_breadcrumb(config.get_option(["finder", "breadcrumb"]))
finder.set_show_hidden_files(config.get_option(["finder", "show_hidden_files"]))
finder.set_show_item_info(config.get_option(["finder", "show_item_info"]))
finder.set_preferred_view_size(config.get_option(["finder", "preferred_view_size"]))
finder.apply()
