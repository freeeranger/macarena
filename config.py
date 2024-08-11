import tomllib
import os
import logger
from utils import text_bold
from typing import List

config = None
default_config = None

def init():
    global config
    global default_config

    if not os.path.exists("./config/config.toml"):
        logger.log_err(f"Failed to find config file {text_bold("config.toml")}", "Initialization phase")
        exit()
    
    if not os.path.exists("./default_config.toml"):
        logger.log_err(f"Failed to find default config file {text_bold("default_config.toml")}", "Initialization phase")
        exit()

    file = open("./config/config.toml", "rb")
    try:
        config = tomllib.load(file)
    except:
        logger.log_err(f"Error encountered in config", "Initialization phase")
        exit()
    
    file = open("./default_config.toml", "rb")
    try:
        default_config = tomllib.load(file)
    except:
        logger.log_err(f"Error encountered in default config", "Initialization phase")
        exit()


def get_option(option: List[str]):
    # try retrieving from config file
    failed = False
    curr_el = config
    for element in option:
        if curr_el is None or element not in curr_el:
            failed = True
            break
        curr_el = curr_el[element]
    if not failed:
        return curr_el
    
    # retrieve value from default config file if not found in config file
    curr_el = default_config
    for element in option:
        if curr_el is None or element not in curr_el:
            break  
        curr_el = curr_el[element]
    return curr_el
