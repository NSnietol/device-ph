import requests
from components.property_manager import get_property_value, get_list_property
from components.property_manager import logger
from components.request_local import post_request
from components.utils.json_util import json_to_obj_latest
from components.utils.bycript_util import generatePassEncripted
from components.utils.json_util import DictObject
from exceptions.internet_exception import WrongCredenciales
from exceptions.sgph_exception import UserNoAllowed
from exceptions.phman_exception import NoGuardFound

def check_guard_permissions(email, id_ph)->bool:
    url = get_property_value("url.phman")+"access/api/v1/vigilants/verify"
    data = {'email': email, 'idPropiedad': id_ph}
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    response = post_request(url, data, headers=headers)
    if(response.status_code == 200):
        return bool(response.content.decode('utf-8'))
    elif response.status_code == 404 :
        raise NoGuardFound("Este {0} no está registrado en el sistema ".format(email))



def check_permissions(user):
    roles = get_allowed_roles(user.roles)
    if(len(roles) > 0):
        return get_current_rol(roles)
    else:
        raise UserNoAllowed()


def get_allowed_roles(roles):
    permissions = get_list_property("internal.permissions")
    return list(set(permissions).intersection(set(roles)))


def get_current_rol(roles):
    return "ADMINISTRADOR" if 'ADMINISTRADOR' in roles else roles[0]
