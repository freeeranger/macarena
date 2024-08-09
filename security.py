import os


def set_sudo_touchid_auth(status):
    # todo add "auth sufficient pam_tid.so" to /etc/pam.d/sudo (needs to do this with sudo access)
    # todo only add if status is True, remove that line instead if status is False
    pass