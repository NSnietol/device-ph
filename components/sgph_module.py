import requests
from http import HTTPStatus

from components.db.db_manager import get_current_user, get_current_device
from components.property_manager import get_property_value, get_list_property
from components.property_manager import logger
from components.request_local import get_request, post_request, get_request_general, get_header_with_auth
from components.utils.json_util import json_to_obj_v2
from components.utils.bycript_util import generatePassEncripted
from components.utils.json_util import DictObject
from exceptions.internet_exception import WrongCredenciales, BadResponse
from exceptions.sgph_exception import NoDeviceFound, UserNoAllowed, NotCommomAreasFound


def do_login(email, password) -> DictObject:
    url = get_property_value("url.sgph")+"auth/signin"
    data = {'email': email, 'password': password}

    response = post_request(url, data, headers=get_header_with_auth())
    if(response.status_code == HTTPStatus.OK):
        usuario = json_to_obj_v2(response.content)
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise WrongCredenciales("Wrong credencials for "+email)
    usuario.password = generatePassEncripted(password)
    check_permissions(usuario)
    return usuario


def check_permissions(user):
    roles = get_allowed_roles(user.roles)
    logger.warning('result', str(roles))
    if(len(roles) > 0):
        return get_current_rol(roles)
    else:
        raise UserNoAllowed()


def get_allowed_roles(roles):
    permissions = get_list_property("internal.permissions")
    logger.info(str(permissions))
    logger.info(roles)
    return list(set(permissions).intersection(set(roles)))


def refresh_login():
    logger.warning("refresh_login")
    current_user = get_current_user()
    if("RASPBERRY_PI" in current_user.roles):
        current_device = get_current_device()
        email = current_device .mac+get_property_value("internal.sufix")
        password = current_device.id
        do_login(email, password)
    else:
        raise NoDeviceFound('Device not found trying to refresh crendecials')


def get_current_rol(roles):
    return "ADMINISTRADOR" if 'ADMINISTRADOR' in roles else roles[0]


def get_area_comunes(id_ph) -> list:
    url = get_property_value("url.sgph")+"bien-comun/listar/"

    response = get_request_general(url, headers=get_header_with_auth(), general={
                                   'params': {'idPropiedadHorizontal': str(id_ph)}})

    if(response.status_code == HTTPStatus.OK):
        return json_to_obj_v2(response.content)
    else:
        raise NotCommomAreasFound()


def get_area_comun(id_area_comun) -> DictObject:
    url = get_property_value("url.sgph")+"bien-comun/"+id_area_comun

    response = get_request(url, headers=get_header_with_auth())
    if(response.status_code == HTTPStatus.OK):
        return response.json()
    else:
        raise NotCommomAreasFound()
