import requests
from requests import Response
from http import HTTPStatus

from components.property_manager import get_property_value,get_list_property
from components.property_manager import logger
from components.connection_local import check_connection
from components.utils.json_util import *
from components.db.db_manager import get_current_device,get_current_user

from exceptions.sgph_exception import NoUserFound



RESPONSE_STATUS = "Response status : "
RETRY_MESSAGE = "Retrying  {0}  the request to {1}"

def post_request(url, body, headers)->Response:
    check_connection()
    body = obj_to_json(body)

    logger.info('POST Request url ' + url)
    logger.info("Request body" + body)
    logger.info("Request headers" + str(headers))
    response = None

    for index in range(1, int(get_property_value("internal.retry.count"))+1):
        try:
            response = requests.post(url=url, data=body, headers=headers)

            if(response.status_code == HTTPStatus.OK):
                logger.debug("Response\n"+ str(response.content))
                break
            elif(response.status_code == HTTPStatus.FORBIDDEN):
                from components.sgph_module import refresh_login
                refresh_login()
                headers = get_header_with_auth()
            else:
                logger.warning(RETRY_MESSAGE.format(index, url))

        except Exception as e:
            logger.exception(e)
            logger.warning(RETRY_MESSAGE.format(index, url))
    logger.info(RESPONSE_STATUS + str(response.status_code))
    logger.debug(response.json())
    return response


def get_request(url, headers)->Response:

    check_connection()

    logger.info('GET Request url ' + url)
    logger.info("Request headers" + str(headers))
    response = None

    for index in range(1, int(get_property_value("internal.retry.count"))+1):
        try:
            response = requests.get(url=url, headers=headers)

            if(response.status_code == HTTPStatus.OK):
                logger.debug("Response", str(response.content))
                break
            elif(response.status_code == HTTPStatus.FORBIDDEN):
                from components.sgph_module import refresh_login
                refresh_login()
                headers = get_header_with_auth()
            else:
                logger.warning(RETRY_MESSAGE.format(index, url))

        except Exception:
             logger.warning(RETRY_MESSAGE.format(index, url))
    logger.info(RESPONSE_STATUS + str(response.status_code))
    return response



def put_request(url, body, headers)->Response:
    check_connection()
    body = obj_to_json(body)

    logger.info('POST Request url ' + url)
    logger.info("Request body" + body)
    logger.info("Request headers" + str(headers))
    response = None

    for index in range(1, int(get_property_value("internal.retry.count"))+1):
        try:
            response = requests.put(url=url, data=body, headers=headers)

            if(response.status_code == HTTPStatus.OK):
                logger.debug("Response\n"+ str(response.content))
                break
            elif(response.status_code == HTTPStatus.FORBIDDEN):
                from components.sgph_module import refresh_login
                refresh_login()
                headers = get_header_with_auth()
            else:
                logger.warning(RETRY_MESSAGE.format(index, url))

        except Exception as e:
            logger.exception(e)
            logger.warning(RETRY_MESSAGE.format(index, url))
    logger.info(RESPONSE_STATUS + str(response.status_code))
    logger.debug(response.json())
    return response


def get_request_general(url, headers, retry_count=5, general={}):

    check_connection()

    logger.info('GET Request url ' + url)
    logger.info("Request headers" + str(headers))
    response = None

    for index in range(1, retry_count):
        try:
            response = requests.get(url=url, headers=headers, **general)

            if(response.status_code == HTTPStatus.OK):
                logger.debug("Response\n"+ str(response.json()))
                break
            elif(response.status_code == HTTPStatus.FORBIDDEN):

                logger.warning('FORBIDDEN Request {0}'.format(url))

                from components.sgph_module import refresh_login
                refresh_login()
                headers = get_header_with_auth()
            else:
                logger.warning(RETRY_MESSAGE.format(index, url))

        except Exception as e:
            logger.exception(e)
            logger.warning(RETRY_MESSAGE.format(index, url))
    logger.info(RESPONSE_STATUS + str(response.status_code))
    logger.debug(response.json())
    return response



def get_header_with_auth():
    default_headers = get_default_headers()

    try:
        default_headers.update({'Authorization':'Bearer '+get_current_user().token})
        logger.info('get_header_with_auth OK')
        return default_headers
    except NoUserFound:
        logger.warning('No user authorization found')
    return default_headers

def get_default_headers():
    headers = get_list_property("internal.headers")
    result_headers = {}
    for header in headers:
        key = header.split("|")[0]
        value = header.split("|")[1]
        result_headers.update({key:value})
    return  result_headers




