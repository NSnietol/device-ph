from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from loguru import logger

from frontend.login import LoginForm
from frontend.main import MainPHWindow
from components.sgph_module import do_login
from exceptions.internet_exception import *
from exceptions.sgph_exception import *
from exceptions.phman_exception import *

from components.utils.thread_util import execute_background
from components.db.db_manager import save_user, get_current_device, get_current_user
from components.sgph_module import get_current_rol, get_persona
from components.phman_module import check_guard_permissions


class BiometricController():

    def __init__(self, biometric_tab):
        self.biometric_tab = biometric_tab

    def search_person(self):

        try:
            person = get_persona(self.biometric_tab.line_edit_identification.text(), self.biometric_tab.combo_box_identification_type.currentText(), 
            self.biometric_tab.combo_box_rol.currentText(), get_current_user().idPropiedadHorizontal)
            self.biometric_tab.line_edit_person_name.setText(
                person.nombres + " "if person.apellido is None else person.apellido)

        except NoPersonFound as person_no_found:
            QtWidgets.QMessageBox.warning(
                None, 'No se pudo completar la operacion', str(person_no_found))
        except Exception as faltal_excep:
            logger.exception(faltal_excep)
            QtWidgets.QMessageBox.warning(
                None, 'No se pudo completar la operacion', '')


def run():

    from frontend.main import MainPHWindow
    from frontend.controllers.main_control import MainController
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = MainPHWindow()
    main_controller = MainController(main)
    main.setupUi(window, main_controller)
    biometric_controller = BiometricController(main)
    main.set_biometric_controller(biometric_controller)

    window.show()
    sys.exit(app.exec_())
