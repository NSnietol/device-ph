from os.path import expanduser
from loguru import logger
import os

from components.property_manager import get_property_value


def get_folder():
    home = expanduser("~")+os.sep+get_property_value("internal.folder")
    create_folder(home)
    return home
    
def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_path(value)->str:
    return os.path.dirname(value)

""" origin_file = __file__ it's the file from you call the method
    packages = it's the path, which is separate with commas e.x 'media','main.css'
"""
def get_path_file(origin_file, packages)->str:
    return os.path.join(get_path(origin_file), *packages)