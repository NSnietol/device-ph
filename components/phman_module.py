import requests
from http import HTTPStatus
from components.property_manager import get_property_value, get_list_property
from components.property_manager import logger
from components.request_local import post_request, put_request, get_header_with_auth
from components.utils.json_util import json_to_obj_v2
from components.utils.bycript_util import generatePassEncripted
from components.utils.json_util import DictObject
from exceptions.internet_exception import WrongCredenciales
from exceptions.sgph_exception import UserNoAllowed
from exceptions.phman_exception import NoGuardFound, CouldntCreateDevice, CouldntUpdateDevice


def check_guard_permissions(email, id_ph) -> bool:
    url = get_property_value("url.phman")+"access/api/v1/vigilants/verify"
    data = {'email': email, 'idPropiedad': id_ph}
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    response = post_request(url, data, headers=headers)
    if(response.status_code == 200):
        return bool(response.content.decode('utf-8'))
    elif response.status_code == 404:
        raise NoGuardFound(
            "Este {0} no está registrado en el sistema ".format(email))


def create_device(device):
    url = get_property_value('url.phman')+"access/api/v1/devices"

    create_device_response = post_request(url, device, get_header_with_auth())

    if(create_device_response.status_code != HTTPStatus.OK):
        raise CouldntCreateDevice()
    else:
        return DictObject(create_device_response.json())


def update_device(device):
    url = get_property_value('url.phman')+"access/api/v1/devices"

    create_device_response = put_request(url, device, get_header_with_auth())

    if(create_device_response.status_code != HTTPStatus.OK):
        if(create_device_response.status_code == 500):
            create_device(device)
        else:
            raise CouldntUpdateDevice()
    else:
        return DictObject(create_device_response.json())


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
