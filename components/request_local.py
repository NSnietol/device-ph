import requests
from components.property_manager import getPropertyValue
from components.property_manager import logger
from components.connection_local import checkConnection
from components.utils.json_util import *


def postRequest(url, body, headers):
    checkConnection()
    body = obj_to_json(body)

    logger.info('Request url ' + url)
    logger.info("Request body" + body)
    logger.info("Request headers" + str(headers))
    response = None

    for index in range(1, int(getPropertyValue("internal.retry.count"))+1):
        try:
            response = requests.post(url=url, data=body, headers=headers)

            if(response.status_code == 200):
                logger.debug("Response", str(response.content))
                break
            else:
                logger.warning("Retrying  {index}  the request to", url)

        except Exception as e:
            logger.warning(
                "Retrying  {0}  the request to {1}".format(index, url))

    return response
