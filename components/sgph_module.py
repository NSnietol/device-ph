import requests
from components.property_manager import get_property_value
from components.property_manager import logger
from components.request_local import post_request
from components.utils.json_util import json_to_obj
from components.utils.file_util import save_user
from exceptions.internet_exception import WrongCredenciales


def do_login(email, password):
    url = get_property_value("url.sgph")+"auth/signin"
    data = {'email': email, 'password': password}
    print(data)
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    logger.info("do_login", data)
    response = post_request(url, data, headers=headers)
    if(response.status_code == 200):
        usuario = json_to_obj(response.content)
    elif response.status_code == 400:
        raise WrongCredenciales("Wrong credencials for "+email)
    save_user(usuario)
    return usuario
