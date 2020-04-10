import requests
from components.property_manager import getPropertyValue
from config.logsmanager import logger
from exceptions.internet_exception import NoInternetException


def checkConnection():
    try:
        for index in range(1,int(getPropertyValue("internal.retry.count"))):
            response = requests.get(getPropertyValue("internal.url.test"))
            if(response.status_code == 200):
                logger.info("Connection OK")
                break
    except requests.exceptions.ConnectionError as econnection:
        logger.info(econnection)
        raise NoInternetException("Sorry! no connection")
        return False
    except Exception as egeneral:
        return False
        logger.warning("Fatal", egeneral)
    return True
