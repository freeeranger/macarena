import os
from typing import List
import logger
from docklib import Dock

def set_tilesize(size: int):
    dock = Dock()
    dock.tilesize = size # type: ignore
    dock.save()

def set_largesize(size: int):
    dock = Dock()
    dock.largesize = size #type: ignore
    dock.save()

def set_orientation(orientation: str):
    dock = Dock()
    dock.orientation = orientation #type: ignore
    dock.save()

def set_magnification(status: bool):
    dock = Dock()
    dock.magnification = status #type: ignore
    dock.save()

def set_autohide(status: bool):
    dock = Dock()
    dock.autohide = status #type: ignore
    dock.save()

def set_show_recents(status: bool):
    dock = Dock()
    dock.show_recents = status #type: ignore
    dock.save()

def set_show_process_indicators(status: bool):
    dock = Dock()
    dock.show_process_indicators = status #type: ignore
    dock.save()

def set_show_progress_indicators(status: bool):
    dock = Dock()
    dock.show_progress_indicators = status #type: ignore
    dock.save()

def set_persistent_apps(apps: List[str]):
    dock = Dock()
    dock.items["persistent-apps"] = []

    for app in apps:
        app = os.path.expanduser(app)

        if not os.path.exists(app):
            logger.log_warn(f"Path {app} does not exist, skipping", "dock.persistent_apps")
            continue
        dock.items["persistent-apps"].append(dock.makeDockAppEntry(app))

    dock.save()

def set_persistent_others(others: List[str]):
    dock = Dock()
    dock.items["persistent-others"] = []

    for other in others:
        other = os.path.expanduser(other)
        if not os.path.exists(other):
            logger.log_warn(f"Path {other} does not exist, skipping", "dock.persistent_others")
            continue
        dock.items["persistent-others"].append(
            dock.makeDockOtherEntry(
                other, 
                displayas=1,
                arrangement=3, 
                showas=1
            )
        )

    dock.save()