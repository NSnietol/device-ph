import sys

from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}")
logger.add("logs/record.log", rotation="15 week")    # Once the file is too old, it's rotated
