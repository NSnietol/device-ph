import requests
from components.property_manager import getPropertyValue
from config.logsmanager import logger
from exceptions.internet_exception import NoInternetException

def checkConnection():
    try:
        requests.get(getPropertyValue("internal.url.test"))
        logger.info("Connection OK")
    except requests.exceptions.ConnectionError as econnection:
        logger.info(econnection)
        return False
    except Exception as egeneral:
        return False
        logger.warning("Fatal",egeneral)
    return True
        