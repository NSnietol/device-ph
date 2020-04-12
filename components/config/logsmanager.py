import sys
from loguru import logger
from os.path import expanduser

import os

from components.property_manager import get_property_value
from components.utils.file_util import get_folder



path = get_folder() + os.sep+get_property_value("internal.log.file")

rotation = get_property_value("internal.log.rotation")

logger.add(sys.stderr, format="{time} {level} {message}")
logger.add(path, rotation=rotation)    # Once the file is too old, it's rotated
