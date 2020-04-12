from components.property_manager import get_property_value
from config.logsmanager import logger


from peewee import *
from os.path import expanduser
import os


home = expanduser("~")+os.sep+get_property_value("internal.folder")

path = home + os.sep+get_property_value("internal.db")


def create_folder():
    if not os.path.exists(home):
        logger.info('Create folder'+home)
        os.mkdir(home)


create_folder()

db = SqliteDatabase(path)


class BaseModel(Model):
    class Meta:
        database = db

