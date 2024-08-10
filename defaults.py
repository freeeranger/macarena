import os

# TODO not working :( (at least not for iterm2)
def set_default(program: str, value: str):
    os.system(f"defaults write {program} {value}")