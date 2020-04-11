import requests
from components.property_manager import get_property_value
from config.logsmanager import logger
from exceptions.internet_exception import NoInternetException


def check_connection():
    try:
        for index in range(1, int(get_property_value("internal.retry.count"))+1):
            response = requests.get(get_property_value("internal.url.test"))
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
