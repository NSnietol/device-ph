from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from loguru import logger
import strgen
import datetime
from frontend.login import LoginForm
from components.sgph_module import do_login
from exceptions.internet_exception import *
from exceptions.sgph_exception import *
from exceptions.phman_exception import *
from peewee import PeeweeException


from components.property_manager import get_list_property
from components.db.db_manager import save_device
from components.utils.thread_util import execute_background
from components.utils.hardware_util import get_device_mac
from components.sgph_module import get_area_comunes
from components.db.db_manager import save_user, get_current_device
from components.sgph_module import get_current_rol
from components.phman_module import check_guard_permissions, create_device,update_device
from components.db.db_manager import get_current_user,save_device

from components.db.db_manager import save_user, get_current_device



class DeviceController():

    def __init__(self, main_ui):
        print('devoce controller')
        self.main_ui = main_ui

    def save_update_device(self):
        constrains = self.contrains()
        print(self.main_ui.combo_box_area_comun.currentData())
        if(constrains == False):
            device = {
                'nombre': self.main_ui.line_edit_nombre_dispositivo_value.text(),
                'propiedadComun': self.main_ui.combo_box_area_comun.currentData().id,
                'propiedadHorizontal': get_current_user().idPropiedadHorizontal,
                'estado': 'ACTIVO',
                'tipo': self.main_ui.combo_box_device_type.currentText(),
                'mac': get_device_mac()+ strgen.StringGenerator("[\d\w]{10}").render(),
                'fechaRegistro':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            there_is_device = False

            try:
                get_current_device()
                there_is_device=True
            except NoDeviceFound :
                pass


            
            try:
                if(there_is_device):
                    logger.warning('update')
                    print('upate')
                    device_response = update_device(device)
                else:
                    print('create')
                    logger.warning('create')
                    device_response=create_device(device)

                save_device(device_response.get_dict()) # Local store
                QtWidgets.QMessageBox.information(None, 'OK','Dispositivo registrado')

            except (CouldntCreateDevice, CouldntUpdateDevice) as create_device_exception:
                QtWidgets.QMessageBox.warning(None, 'No se pudo completar la operacion',str(create_device_exception))
            except PeeweeException as critical:
                logger.exception(critical)
                QtWidgets.QMessageBox.warning(None, 'No se pudo completar la operacion','Localmente no se pudo guardar el dispositivo')

          

        #raise NoPermissionFound()


    def contrains(self):
        constrains_value = False
        if(self.main_ui.combo_box_device_type.currentIndex() <= 0):
            constrains_value = True
            QtWidgets.QMessageBox.information(
                None, 'Dados faltantes', 'Seleccionar tipo de dispositivo')
        if(self.main_ui.combo_box_area_comun.currentIndex() <= 0):
            constrains_value = True
            QtWidgets.QMessageBox.information(
                None, 'Dados faltantes', 'Seleccionar el area comun')
        if(not self.main_ui.line_edit_nombre_dispositivo_value.text()):
            constrains_value = True
            QtWidgets.QMessageBox.information(
                None, 'Dados faltantes', 'Ingrese el nombre')
        return constrains_value

        
    def default_value(self):
     
        self.request_values_device()
        self.load_device()    

    def load_device(self):
        self.main_ui.label_mac_value.setText(str(get_device_mac()))
        try:
            device = get_current_device()
            self.main_ui.line_edit_nombre_dispositivo_value.setText(device.nombre)
            self.main_ui.label_mac_value.setText(get_device_mac())
            self.main_ui.label_estado_dispositivo_value.setText(device.estado)

            index = self.main_ui.combo_box_device_type.findText(device.tipo, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.main_ui.combo_box_device_type.setCurrentIndex(index)
 


            self.main_ui.set_status(device.estado)

        except NoDeviceFound as no_device:
            logger.exception(no_device)

    def request_values_device(self):
        
        self.main_ui.combo_box_device_type.addItems( ['Lector de matrícula','Lector de huella digital'])
        execute_background(self.requesting_commom_areas)


    def requesting_commom_areas(self):

        try:
            commom_areas = get_area_comunes(get_current_user().idPropiedadHorizontal)
            for area in commom_areas:
                self.main_ui.combo_box_area_comun.addItem(area.nombre,userData=area)

       
        except NotCommomAreasFound as no_commom_area_excep:
            logger.exception(no_commom_area_excep)
            QtWidgets.QMessageBox.information(None,'Sorry',str(no_commom_area_excep))



def run():
    from frontend.main import MainPHWindow
    from frontend.controllers.main_control import MainController
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = MainPHWindow()
    main_controller = MainController(main)
    main.setupUi(window, main_controller)
    device_controller = DeviceController(main)
    main.set_device_controller(device_controller)

    window.show()
    sys.exit(app.exec_())
