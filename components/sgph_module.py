import requests
from components.property_manager import getPropertyValue
from components.property_manager import logger
from components.request_local import postRequest
from components.utils.json_util import json_to_obj
from exceptions.internet_exception import WrongCredenciales


def do_login(email, password):
    url = getPropertyValue("url.sgph")+"auth/signin"
    data = {'email': email, 'password': password}
    print(data)
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    logger.info("do_login", data)
    response = postRequest(url, data, headers=headers)
    if(response.status_code == 200):
        usuario = json_to_obj(response.content)
    elif response.status_code == 400:
        raise WrongCredenciales("Wrong credencials for "+email)

    return usuario

