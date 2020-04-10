from components.request_local import get_request
from components.property_manager import get_property_value
from components.utils.json_util import json_to_obj
from config.logsmanager import logger
from exceptions.phman_exception import NoReservationsFound, NoResidentsFound


import time
import threading

INTERVAL_TIME_TO_UPDATE = int(
    get_property_value("internal.frecuency") or 3600*3)
# FLAG_PREVIUS_STATUS


def sync_phman():
    logger.info("INIT SYNC TASK")
    sync_phman_people()
    sync_phman_reservations()
    logger.info("SCHEDULED SYNC TASK")


def sync_phman_people():
    try:

        get_all_people(14)
        logger.info("PEOPLE'S UPDATED")
        # FLAG_PREVIUS_STATUS=True
    except NoResidentsFound:
        logger.error("Error sync_phman_all_people")

    except Exception as identifier:
        logger.critical("Error sync_phman previous status ")
        logger.critical(identifier)
    finally:
        logger.info("SCHEDULING PEOPLE TASK AGAIN ;)")
        threading.Timer(INTERVAL_TIME_TO_UPDATE, sync_phman_people).start()


def sync_phman_reservations():
    try:

        get_all_reservations(14)
        logger.info("RESEVARTION'S UPDATED")

    except NoReservationsFound:
        logger.error("Error sync_phman_all_reservations")
    except Exception as identifier:
        logger.critical("Error sync_phman previous status")
        logger.critical(identifier)
    finally:
        logger.info("SCHEDULE RESEVATIONS TASK AGAIN ;)")
        threading.Timer(INTERVAL_TIME_TO_UPDATE,
                        sync_phman_reservations).start()



def get_all_people(id_ph):
    url = get_property_value("url.phman") + \
        "access/api/v1/persons/phs/{0}".format(id_ph)

    response = get_request(url, None)
    if(response.status_code > 400 and response.status_code < 500):
        raise NoResidentsFound(str(response.text))
    return json_to_obj(response.content)


def get_all_reservations(id):
    raise Exception("No implemented yet")
