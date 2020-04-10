
from config.logsmanager import logger

import os


def getEnvironment():

    return os.getenv("env") if os.getenv("env") is not None else "dev"


def getPropertyValue(property):
    logger.info("Get property : " + property + " env :" + getEnvironment())
    response = os.getenv(property)
    if(response is None):
        return os.getenv(getEnvironment()+"."+property)
    else:
        return response
