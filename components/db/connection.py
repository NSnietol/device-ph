from components.property_manager import get_property_value
from components.config.logsmanager import logger
from components.utils.file_util import get_folder


from peewee import *
from os.path import expanduser
import os


home = get_folder()

path = home + os.sep+get_property_value("internal.db")

db = SqliteDatabase(path)


class BaseModel(Model):
    class Meta:
        database = db
