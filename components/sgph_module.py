import requests
from components.property_manager import get_property_value, get_list_property
from components.property_manager import logger
from components.request_local import post_request
from components.utils.json_util import json_to_obj_latest
from components.utils.bycript_util import generatePassEncripted
from components.utils.json_util import DictObject
from exceptions.internet_exception import WrongCredenciales
from exceptions.sgph_exception import UserNoAllowed


def do_login(email, password)->DictObject:
    url = get_property_value("url.sgph")+"auth/signin"
    data = {'email': email, 'password': password}
    print(data)
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    response = post_request(url, data, headers=headers)
    if(response.status_code == 200):
        usuario = json_to_obj_latest(response.content)
    elif response.status_code == 400:
        raise WrongCredenciales("Wrong credencials for "+email)
    usuario.password = generatePassEncripted(password)
    check_permissions(usuario)
    return usuario


def check_permissions(user):
    roles = get_allowed_roles(user.roles)
    logger.warning('result',str(roles))
    if(len(roles) > 0):
        return get_current_rol(roles)
    else:
        raise UserNoAllowed()


def get_allowed_roles(roles):
    permissions = get_list_property("internal.permissions")
    logger.info(str(permissions))
    logger.info(roles)
    return list(set(permissions).intersection(set(roles)))


def get_current_rol(roles):
    return "ADMINISTRADOR" if 'ADMINISTRADOR' in roles else roles[0]
