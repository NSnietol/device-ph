from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from loguru import logger

from frontend.login import LoginForm
from components.sgph_module import do_login
from exceptions.internet_exception import *
from exceptions.sgph_exception import *
from exceptions.phman_exception import *

from components.utils.thread_util import execute_background
from components.db.db_manager import save_user, get_current_device
from components.sgph_module import get_current_rol
from components.phman_module import check_guard_permissions


class LoginController():

    def __init__(self, login_ui):
        print('Init controller')
        self.login_ui = login_ui

    def login_sgph(self):
        self.login_method()

    def login_method(self):
        try:
            user = do_login(self.login_ui.line_edit_usuario.text(),
                            self.login_ui.line_edit_password.text())

            if(get_current_rol(user.roles) != 'ADMINISTRADOR'):

                device = get_current_device()
                device.propiedadHorizontal
                user.propiedadHorizontal = device.propiedadHorizontal
                permissions_ph = check_guard_permissions(user.email, device.propiedadHorizontal)
                if(permissions_ph == False):
                    raise NoPermissionFound()
                else:
                    save_user(save_user.get_dict())

            else:
                save_user(save_user.get_dict())

        except NoDeviceFound as no_device:
            QtWidgets.QMessageBox.warning(None, 'WARNING', str(no_device))
        except NoInternetException as no_internet:
            QtWidgets.QMessageBox.warning(None, 'WARNING', str(no_internet))
        except WrongCredenciales as wrong_cre:
            QtWidgets.QMessageBox.warning(None, 'WARNING', str(wrong_cre))
        except NoGuardFound as no_guard:
            QtWidgets.QMessageBox.warning(None, 'WARNING', str(no_guard))
        except UserNoAllowed as user_no:
            QtWidgets.QMessageBox.warning(None, 'WARNING', str(user_no))

        except Exception as e:
            logger.warning(str(e))
            QtWidgets.QMessageBox.warning(
                None, 'WARNING', 'ERROR 500, contactar al equipo de soporte')


def run():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoginForm()
    loginContoller = LoginController(ui)
    ui.setupUi(Dialog, loginContoller)
    Dialog.show()
    sys.exit(app.exec_())
