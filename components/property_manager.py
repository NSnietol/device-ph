from loguru import logger
import os


def get_environment():
    return os.getenv("env") if os.getenv("env") is not None else "dev"


def get_property_value(property):
    logger.info("Get property : " + property)
    response = os.getenv(property)
    if(response is None):
        return os.getenv(get_environment()+"."+property)
    else:
        return response

def get_list_property(property):
    return get_property_value(property).split(",")