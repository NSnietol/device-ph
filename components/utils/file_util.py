
import pickle
from components.property_manager import get_property_value
from config.logsmanager import logger

from os.path import expanduser
import os

home = expanduser("~")+os.sep+get_property_value("internal.user.folder")

path = home + os.sep+get_property_value("internal.user.name")




def create_folder():
    if not os.path.exists(home):
        logger.info('Create folder'+home)
        os.mkdir(home)


create_folder()


def save_user(usuario):
    logger.info('saving user ',usuario.email)
    pickle.dump(usuario, open(path, "wb"))


def get_user():
    logger.info('getting user ')
    return pickle.load(open(path, "rb"))

