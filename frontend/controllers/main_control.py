# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from loguru import logger

from frontend.login import LoginForm
from components.sgph_module import do_login
from exceptions.internet_exception import *
from exceptions.sgph_exception import *
from exceptions.phman_exception import *


from components.utils import thread_util
from components.property_manager import get_list_property
from components.utils.thread_util import execute_background
from components.utils.hardware_util import get_device_mac
from components.sgph_module import get_area_comunes
from components.db.db_manager import save_user, get_current_device
from components.sgph_module import get_current_rol
from components.phman_module import check_guard_permissions
from components.db.db_manager import get_current_user
from frontend.main import MainPHWindow
from components.db.db_manager import save_user, get_current_device
from frontend.controllers.device_controller import DeviceController


class MainController():

    def __init__(self, main_ui):
        print('main controller')
        self.main_ui = main_ui
        self.device_controller = DeviceController(main_ui)
        self.main_ui.set_device_controller(self.device_controller)
        

    def set_email(self):
        self.main_ui.action_cerrar_usuario.setText("Cerrar sesion :"+get_current_user().email)
   
    def set_default_values(self):
        self.set_email()
        try:
            get_current_device()
     
        except NoDeviceFound as no_device:
            QtWidgets.QMessageBox.information(None,'Debemos registrar este dipositivo',str(no_device))
        self.device_controller.default_value()



def run():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = MainPHWindow()
    main_controller = MainController(main)
    main.setupUi(window, main_controller)
    window.show()
    sys.exit(app.exec_())