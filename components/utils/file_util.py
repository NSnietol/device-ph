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
        logger.info('Create folder'+folder)
        os.mkdir(folder)