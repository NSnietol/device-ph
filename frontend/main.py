# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ph_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
import os
from components.utils.thread_util import execute_background

from components.utils.file_util import get_path_file


class MainPHWindow(object):
    def setupUi(self, main_ph_window, main_controller):
        self.main_controller = main_controller
        self.main_ph_window = main_ph_window
        self.main_ph_window.setObjectName("main_ph_window")
        self.main_ph_window.resize(1190, 711)
        self.main_ph_window.setStyleSheet(
            open(get_path_file(__file__, ['css', 'main-style.css'])).read())

        self.centralwidget = QtWidgets.QWidget(self.main_ph_window)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(230, 60, 911, 531))
        self.tab_widget.setObjectName("tab_widget")
        self.group_box_contenedor_opciones = QtWidgets.QGroupBox(
            self.centralwidget)
        self.group_box_contenedor_opciones.setGeometry(
            QtCore.QRect(40, 60, 181, 531))
        self.group_box_contenedor_opciones.setTitle("")
        self.group_box_contenedor_opciones.setObjectName(
            "group_box_contenedor_opciones")
        self.push_button_registar_huella = QtWidgets.QPushButton(
            self.group_box_contenedor_opciones)
        self.push_button_registar_huella.setGeometry(
            QtCore.QRect(0, 170, 181, 111))
        self.push_button_registar_huella.setObjectName(
            "push_button_registar_huella")
        self.push_button_estado_dispositivo = QtWidgets.QPushButton(
            self.group_box_contenedor_opciones)
        self.push_button_estado_dispositivo.setGeometry(
            QtCore.QRect(0, 0, 181, 111))
        self.push_button_estado_dispositivo.setObjectName(
            "push_button_estado_dispositivo")
        self.label_estado_main_dispositivo = QtWidgets.QLabel(
            self.centralwidget)
        self.label_estado_main_dispositivo.setGeometry(
            QtCore.QRect(50, 630, 161, 16))
        self.label_estado_main_dispositivo.setObjectName(
            "label_estado_main_dispositivo")
        self.main_ph_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_ph_window)
        self.statusbar.setObjectName("statusbar")
        self.main_ph_window.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self.main_ph_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 23))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuacerca_de_ph_man = QtWidgets.QMenu(self.menubar)
        self.menuacerca_de_ph_man.setObjectName("menuacerca_de_ph_man")
        self.main_ph_window.setMenuBar(self.menubar)
        self.actionAgregar_residente = QtWidgets.QAction(self.main_ph_window)
        self.actionAgregar_residente.setObjectName("actionAgregar_residente")
        self.actionAgregar_visitante = QtWidgets.QAction(self.main_ph_window)
        self.actionAgregar_visitante.setObjectName("actionAgregar_visitante")
        self.actionAccionar_compuerta = QtWidgets.QAction(self.main_ph_window)
        self.actionAccionar_compuerta.setObjectName("actionAccionar_compuerta")
        self.action_cerrar_usuario = QtWidgets.QAction(self.main_ph_window)
        self.action_cerrar_usuario.setObjectName("action_cerrar_usuario")
        self.actionActivar_persona = QtWidgets.QAction(self.main_ph_window)
        self.actionActivar_persona.setObjectName("actionActivar_persona")
        self.menuOpciones.addAction(self.action_cerrar_usuario)
        self.menuOpciones.addSeparator()
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuacerca_de_ph_man.menuAction())

        self.retranslateUi(self.main_ph_window)

        QtCore.QMetaObject.connectSlotsByName(self.main_ph_window)
        self.load_tabs()
        self.set_view_estado_dispositivo()

        self.preferences()
        self.set_icons()
        self.events()
        self.load_default_values()

    def retranslateUi(self, main_ph_window):
        _translate = QtCore.QCoreApplication.translate
        self.main_ph_window.setWindowTitle(
            _translate("main_ph_window", "PH MAN"))
        self.push_button_registar_huella.setText(
            _translate("main_ph_window", "Biometria"))
        self.push_button_estado_dispositivo.setText(
            _translate("main_ph_window", "Estado del dispositivo"))
        self.label_estado_main_dispositivo.setText(
            _translate("main_ph_window", "Estado de conexion"))
        self.menuOpciones.setTitle(_translate("main_ph_window", "Opciones"))
        self.menuacerca_de_ph_man.setTitle(
            _translate("main_ph_window", "acerca de PH MAN"))
        self.actionAgregar_residente.setText(
            _translate("main_ph_window", "Agregar residente"))
        self.actionAgregar_visitante.setText(
            _translate("main_ph_window", "Agregar visitante"))
        self.actionAccionar_compuerta.setText(
            _translate("main_ph_window", "Accionar compuerta"))
        self.action_cerrar_usuario.setText(
            _translate("main_ph_window", "Cerrar usuario : "))
        self.actionActivar_persona.setText(
            _translate("main_ph_window", "Activar persona"))

    def set_icons(self):
        self.push_button_registar_huella.setIcon(qta.icon('fa5s.fingerprint'))
        self.push_button_registar_huella.setIconSize(QtCore.QSize(45, 40))

        self.push_button_estado_dispositivo.setIcon(
            qta.icon('fa5s.laptop-code'))
        self.push_button_estado_dispositivo.setIconSize(QtCore.QSize(45, 40))

    def preferences(self):
        self.main_ph_window.setWindowIcon(QtGui.QIcon(
            get_path_file(__file__, ['media', 'user.png'])))
        self.tab_widget.setCurrentIndex(0)
        self.center()

    def center(self):
        q_rect = self.main_ph_window.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        q_rect.moveCenter(center_point)
        self.main_ph_window.move(q_rect.topLeft())

    def events(self):
        self.push_button_estado_dispositivo.clicked.connect(
            self.set_focus_device)
        self.push_button_registar_huella.clicked.connect(
            self.set_view_finger_print)
        self.push_button_registrar_dispositivo.clicked.connect(
            self.update_create_device)
        self.push_button_search.clicked.connect(self.search_person)
        self.push_button_fingerprint.clicked.connect(self.update_fingerprint)

    def set_status(self, value: str):
        self.label_estado_main_dispositivo.setText(
            'Dispositivo {0}'.format(value))

    def set_focus_device(self):
        self.set_view_estado_dispositivo()

    def load_tabs(self):
        self.tab_device_ui_elements()
        self.tab_biometric_ui_elements()

    def tab_device_ui_elements(self):
        self.tab_fingerprint = QtWidgets.QWidget()
        self.tab_fingerprint.setObjectName("tab_fingerprint")
        self.group_box_inside_dispositivo = QtWidgets.QGroupBox(
            self.tab_fingerprint)
        self.group_box_inside_dispositivo.setGeometry(
            QtCore.QRect(50, 50, 711, 401))
        self.group_box_inside_dispositivo.setObjectName(
            "group_box_inside_dispositivo")
        self.line_edit_nombre_dispositivo_value = QtWidgets.QLineEdit(
            self.group_box_inside_dispositivo)
        self.line_edit_nombre_dispositivo_value.setGeometry(
            QtCore.QRect(220, 30, 241, 31))
        self.line_edit_nombre_dispositivo_value.setStyleSheet("D{\n"
                                                              "\n"
                                                              "background: rgb(255, 0, 255)\n"
                                                              "}")
        self.line_edit_nombre_dispositivo_value.setObjectName(
            "line_edit_nombre_dispositivo_value")
        self.label_nombre_dispositivo = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_nombre_dispositivo.setGeometry(
            QtCore.QRect(10, 30, 181, 20))
        self.label_nombre_dispositivo.setObjectName("label_nombre_dispositivo")
        self.label_device_type = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_device_type.setGeometry(QtCore.QRect(10, 80, 181, 20))
        self.label_device_type.setObjectName("label_device_type")
        self.combo_box_device_type = QtWidgets.QComboBox(
            self.group_box_inside_dispositivo)
        self.combo_box_device_type.setEnabled(True)
        self.combo_box_device_type.setGeometry(QtCore.QRect(220, 70, 241, 31))
        self.combo_box_device_type.setObjectName("combo_box_device_type")
        self.combo_box_device_type.addItem("")
        self.push_button_registrar_dispositivo = QtWidgets.QPushButton(
            self.group_box_inside_dispositivo)
        self.push_button_registrar_dispositivo.setGeometry(
            QtCore.QRect(220, 300, 241, 31))
        self.push_button_registrar_dispositivo.setObjectName(
            "push_button_registrar_dispositivo")
        self.label_mac = QtWidgets.QLabel(self.group_box_inside_dispositivo)
        self.label_mac.setGeometry(QtCore.QRect(10, 180, 181, 20))
        self.label_mac.setObjectName("label_mac")
        self.label_mac_value = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_mac_value.setGeometry(QtCore.QRect(220, 180, 241, 20))
        self.label_mac_value.setText("")
        self.label_mac_value.setObjectName("label_mac_value")
        self.label_estado_dispositivo = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_estado_dispositivo.setGeometry(
            QtCore.QRect(10, 220, 181, 20))
        self.label_estado_dispositivo.setObjectName("label_estado_dispositivo")
        self.label_estado_dispositivo_value = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_estado_dispositivo_value.setGeometry(
            QtCore.QRect(220, 220, 241, 20))
        self.label_estado_dispositivo_value.setObjectName(
            "label_estado_dispositivo_value")
        self.label_area_comun = QtWidgets.QLabel(
            self.group_box_inside_dispositivo)
        self.label_area_comun.setGeometry(QtCore.QRect(10, 130, 181, 20))
        self.label_area_comun.setObjectName("label_area_comun")
        self.combo_box_area_comun = QtWidgets.QComboBox(
            self.group_box_inside_dispositivo)
        self.combo_box_area_comun.setEnabled(True)
        self.combo_box_area_comun.setGeometry(QtCore.QRect(220, 120, 241, 31))
        self.combo_box_area_comun.setObjectName("combo_box_area_comun")
        self.combo_box_area_comun.addItem("")
        self.tab_widget.addTab(self.tab_fingerprint, "")
        self.tab_widget.setStyleSheet(
            open(get_path_file(__file__, ['css', 'hide-tabs-style.css'])).read())
        self.retranslate_ui_device()

    def retranslate_ui_device(self):
        _translate = QtCore.QCoreApplication.translate
        self.group_box_inside_dispositivo.setTitle(
            _translate("Dialog", "Info del dispositivo"))
        self.label_nombre_dispositivo.setText(
            _translate("Dialog", "Nombre del dispositivo"))
        self.label_device_type.setText(
            _translate("Dialog", "Tipo de dispositivo"))
        self.combo_box_device_type.setItemText(
            0, _translate("Dialog", "Seleccionar"))
        self.push_button_registrar_dispositivo.setText(
            _translate("Dialog", "Actualizar"))
        self.label_mac.setText(_translate("Dialog", "MAC ( ID UNICO)"))
        self.label_estado_dispositivo.setText(_translate("Dialog", "ESTADO "))
        self.label_estado_dispositivo_value.setText(
            _translate("Dialog", "INACTIVO"))
        self.label_area_comun.setText(_translate("Dialog", "Area común"))
        self.combo_box_area_comun.setItemText(
            0, _translate("Dialog", "Seleccionar"))

    def tab_biometric_ui_elements(self):
        self.tab_fingerprint = QtWidgets.QWidget()
        self.tab_fingerprint.setObjectName("tab_fingerprint")

        self.group_box_information = QtWidgets.QGroupBox(
            self.tab_fingerprint)
        self.group_box_information.setGeometry(QtCore.QRect(40, 20, 621, 231))
        self.group_box_information.setMinimumSize(QtCore.QSize(621, 0))
        self.group_box_information.setObjectName("group_box_information")
        self.combo_box_identification_type = QtWidgets.QComboBox(
            self.group_box_information)
        self.combo_box_identification_type.setGeometry(
            QtCore.QRect(290, 80, 271, 31))
        self.combo_box_identification_type.setObjectName(
            "combo_box_identification_type")
        self.combo_box_identification_type.addItem("")
        self.combo_box_identification_type.addItem("")
        self.combo_box_identification_type.addItem("")
        self.label_identification_type = QtWidgets.QLabel(
            self.group_box_information)
        self.label_identification_type.setGeometry(
            QtCore.QRect(20, 90, 241, 21))
        self.label_identification_type.setObjectName(
            "label_identification_type")
        self.label_identification_value = QtWidgets.QLabel(
            self.group_box_information)
        self.label_identification_value.setGeometry(
            QtCore.QRect(20, 130, 241, 31))
        self.label_identification_value.setObjectName(
            "label_identification_value")
        self.line_edit_identification = QtWidgets.QLineEdit(
            self.group_box_information)
        self.line_edit_identification.setGeometry(
            QtCore.QRect(290, 130, 271, 31))
        self.line_edit_identification.setObjectName("line_edit_identification")
        self.push_button_search = QtWidgets.QPushButton(
            self.group_box_information)
        self.push_button_search.setGeometry(QtCore.QRect(290, 170, 271, 31))
        self.push_button_search.setStyleSheet("\n"
                                              "border-radius: 10px;\n"
                                              "")
        self.push_button_search.setObjectName("push_button_search")
        self.label_rol_value = QtWidgets.QLabel(self.group_box_information)
        self.label_rol_value.setGeometry(QtCore.QRect(20, 30, 241, 31))
        self.label_rol_value.setObjectName("label_rol_value")
        self.combo_box_rol = QtWidgets.QComboBox(self.group_box_information)
        self.combo_box_rol.setGeometry(QtCore.QRect(290, 30, 271, 31))
        self.combo_box_rol.setObjectName("combo_box_rol")
        self.combo_box_rol.addItem("")
        self.combo_box_rol.addItem("")
        self.group_box_people = QtWidgets.QGroupBox(
            self.tab_fingerprint)
        self.group_box_people.setGeometry(QtCore.QRect(40, 260, 621, 261))
        self.group_box_people.setStyleSheet("QPushButton{\n"
                                            "background: rgb(93, 242, 214);\n"
                                            "}")
        self.group_box_people.setObjectName("group_box_people")
        self.push_button_save_biometric_data = QtWidgets.QPushButton(
            self.group_box_people)
        self.push_button_save_biometric_data.setGeometry(
            QtCore.QRect(290, 200, 271, 41))
        self.push_button_save_biometric_data.setStyleSheet("\n"
                                                           "border-radius: 10px;\n"
                                                           "\n"
                                                           "")
        self.push_button_save_biometric_data.setObjectName(
            "push_button_save_biometric_data")
        self.label_actualizar_huella = QtWidgets.QLabel(self.group_box_people)
        self.label_actualizar_huella.setGeometry(QtCore.QRect(20, 40, 241, 31))
        self.label_actualizar_huella.setObjectName("label_actualizar_huella")
        self.push_button_fingerprint = QtWidgets.QPushButton(
            self.group_box_people)
        self.push_button_fingerprint.setGeometry(
            QtCore.QRect(290, 40, 271, 31))
        self.push_button_fingerprint.setStyleSheet("\n"
                                                   "border-radius: 10px;\n"
                                                   "")
        self.push_button_fingerprint.setObjectName("push_button_fingerprint")
        self.label_names = QtWidgets.QLabel(self.group_box_people)
        self.label_names.setGeometry(QtCore.QRect(20, 100, 241, 31))
        self.label_names.setObjectName("label_names")
        self.line_edit_person_name = QtWidgets.QLineEdit(self.group_box_people)
        self.line_edit_person_name.setEnabled(False)
        self.line_edit_person_name.setGeometry(QtCore.QRect(290, 100, 271, 31))
        self.line_edit_person_name.setObjectName("line_edit_person_name")
        self.tab_widget.addTab(self.tab_fingerprint, "")
        self.retranslate_ui_fingerprint()

    def retranslate_ui_fingerprint(self):
        _translate = QtCore.QCoreApplication.translate

        self.group_box_information.setTitle(
            _translate("Dialog", "Información"))
        self.combo_box_identification_type.setItemText(
            0, _translate("Dialog", "CC"))
        self.combo_box_identification_type.setItemText(
            1, _translate("Dialog", "DNI"))
        self.combo_box_identification_type.setItemText(
            2, _translate("Dialog", "TI"))
        self.combo_box_identification_type.setItemText(
            3, _translate("Dialog", "CE"))
        self.combo_box_identification_type.setItemText(
            4, _translate("Dialog", "Pasaporte"))
        self.label_identification_type.setText(
            _translate("Dialog", "Tipo de identificación"))
        self.label_identification_value.setText(
            _translate("Dialog", "Numero de identificación"))
        self.push_button_search.setText(_translate("Dialog", "Buscar"))
        self.label_rol_value.setText(_translate("Dialog", "Rol "))
        self.combo_box_rol.setItemText(
            1, _translate("Dialog", "PERSONAL DE SOPORTE"))
        self.combo_box_rol.setItemText(0, _translate("Dialog", "RESIDENTE"))
        self.group_box_people.setTitle(
            _translate("Dialog", "Datos de la persona"))
        self.push_button_save_biometric_data.setText(
            _translate("Dialog", "Guardar"))
        self.label_actualizar_huella.setText(
            _translate("Dialog", "Actualizar huella"))
        self.push_button_fingerprint.setText(
            _translate("Dialog", "Actualizar"))
        self.label_names.setText(_translate("Dialog", "Nombres "))

    def set_device_controller(self, controller):
        self.device_controller = controller

    def set_biometric_controller(self, controller):
        self.biometric_controller = controller

    def set_view_estado_dispositivo(self):
        self.tab_widget.setCurrentIndex(0)

    def set_view_finger_print(self):
        self.tab_widget.setCurrentIndex(1)

    def load_default_values(self):
        self.main_controller.set_default_values()

    def update_create_device(self):
        self.device_controller.save_update_device()
        self.combo_box_device_type.currentText()

    def search_person(self):
        self.biometric_controller.search_person()

    def update_fingerprint(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ph_window = QtWidgets.QMainWindow()
    ui = MainPHWindow()
    ui.setupUi(main_ph_window)
    main_ph_window.show()
    sys.exit(app.exec_())
