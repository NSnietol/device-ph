from models.db_models import *
from components.utils.hardware_util import get_device_mac
from exceptions.sgph_exception import NoUserFound, NoDeviceFound

from loguru import *
from peewee import PeeweeException


def save_user(user):
    """A dict is required """
    delete_tmp_users()
    try:
        return Usuario.create(**user)
    except PeeweeException:
        return Usuario.create(**user)


def delete_tmp_users():
    Usuario.delete().where(Usuario.roles in [
        'SUPER_ADMINISTRADOR', 'ADMINISTRADOR', 'VIGILANTE']).execute()


def save_device(device):
    Dispositivo.delete().where(get_device_mac() == Dispositivo.mac).execute()
    try:
        return Dispositivo.create(**device)
    except PeeweeException:
        return Dispositivo.create(**device)


def get_current_device():
    devices = Dispositivo.select()
    if(len(devices) > 0):
        logger.info('Current device '+devices[0].mac)
        return devices[0]
    else:
        raise NoDeviceFound('Dispositivo no registrado, contacte el admin')


def get_current_user():
    users = Usuario.select()
    if(len(users) > 0):
        logger.info('Current user '+users[0].email)
        return users[0]
    else:
        raise NoUserFound()
