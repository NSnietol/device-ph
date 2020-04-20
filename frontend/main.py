# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ph_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
import os

from components.utils.file_util import get_path_file

class MainPHWindow(object):
    def setupUi(self, main_ph_window,main_controller):
        self.main_controller = main_controller
        self.main_ph_window= main_ph_window
        self.main_ph_window.setObjectName("main_ph_window")
        self.main_ph_window.resize(1190, 711)
        self.main_ph_window.setStyleSheet(open(get_path_file(__file__,[ 'css', 'main-style.css']) ).read())

        self.centralwidget = QtWidgets.QWidget(self.main_ph_window)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(230, 60, 911, 531))
        self.tab_widget.setObjectName("tab_widget")
        self.group_box_contenedor_opciones = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_contenedor_opciones.setGeometry(QtCore.QRect(40, 60, 181, 531))
        self.group_box_contenedor_opciones.setTitle("")
        self.group_box_contenedor_opciones.setObjectName("group_box_contenedor_opciones")
        self.push_button_registar_huella = QtWidgets.QPushButton(self.group_box_contenedor_opciones)
        self.push_button_registar_huella.setGeometry(QtCore.QRect(0, 170, 181, 111))
        self.push_button_registar_huella.setObjectName("push_button_registar_huella")
        self.push_button_estado_dispositivo = QtWidgets.QPushButton(self.group_box_contenedor_opciones)
        self.push_button_estado_dispositivo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.push_button_estado_dispositivo.setObjectName("push_button_estado_dispositivo")
        self.label_estado_dispositivo = QtWidgets.QLabel(self.centralwidget)
        self.label_estado_dispositivo.setGeometry(QtCore.QRect(50, 630, 161, 16))
        self.label_estado_dispositivo.setObjectName("label_estado_dispositivo")
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
        self.load_default_values()
        self.preferences()
        self.set_icons()
        self.events()
      

    def retranslateUi(self, main_ph_window):
        _translate = QtCore.QCoreApplication.translate
        self.main_ph_window.setWindowTitle(_translate("main_ph_window", "PH MAN"))
        self.push_button_registar_huella.setText(_translate("main_ph_window", "Biometria"))
        self.push_button_estado_dispositivo.setText(_translate("main_ph_window", "Estado del dispositivo"))
        self.label_estado_dispositivo.setText(_translate("main_ph_window", "Estado de conexion"))
        self.menuOpciones.setTitle(_translate("main_ph_window", "Opciones"))
        self.menuacerca_de_ph_man.setTitle(_translate("main_ph_window", "acerca de PH MAN"))
        self.actionAgregar_residente.setText(_translate("main_ph_window", "Agregar residente"))
        self.actionAgregar_visitante.setText(_translate("main_ph_window", "Agregar visitante"))
        self.actionAccionar_compuerta.setText(_translate("main_ph_window", "Accionar compuerta"))
        self.action_cerrar_usuario.setText(_translate("main_ph_window", "Cerrar usuario : "))
        self.actionActivar_persona.setText(_translate("main_ph_window", "Activar persona"))

    
    def set_icons(self):
        self.push_button_registar_huella.setIcon(qta.icon('fa5s.fingerprint'))
        self.push_button_registar_huella.setIconSize(QtCore.QSize(45,40))

    
        self.push_button_estado_dispositivo.setIcon( qta.icon('fa5s.laptop-code'))
        self.push_button_estado_dispositivo.setIconSize(QtCore.QSize(45,40))

    
    def preferences(self):
        self.main_ph_window.setWindowIcon(QtGui.QIcon(get_path_file(__file__,['media','user.png'])))
        self.tab_widget.setCurrentIndex(0)
        self.center()


    def center(self):
        q_rect = self.main_ph_window.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        q_rect.moveCenter(center_point)
        self.main_ph_window.move(q_rect.topLeft())

    def events(self):
        self.push_button_estado_dispositivo.clicked.connect(self.set_focus_device)
        self.push_button_registar_huella.clicked.connect(self.set_focus_device)
    

    def set_focus_device(self):
        print('Value',self.tab_widget.count())
        self.set_view_estado_dispositivo()

    def load_tabs(self):
        print('TAS')
        self.tab_device_ui_elements()
    

    def tab_device_ui_elements(self):
        self.tabRegistroSalida = QtWidgets.QWidget()
        self.tabRegistroSalida.setObjectName("tabRegistroSalida")
        self.groupBoxDatosVisitaSalida = QtWidgets.QGroupBox(self.tabRegistroSalida)
        self.groupBoxDatosVisitaSalida.setGeometry(QtCore.QRect(30, 10, 771, 491))
        self.groupBoxDatosVisitaSalida.setStyleSheet("")
        self.groupBoxDatosVisitaSalida.setObjectName("groupBoxDatosVisitaSalida")
        self.groupBoxIdentificarVisitante = QtWidgets.QGroupBox(self.groupBoxDatosVisitaSalida)
        self.groupBoxIdentificarVisitante.setGeometry(QtCore.QRect(20, 30, 711, 321))
        self.groupBoxIdentificarVisitante.setObjectName("groupBoxIdentificarVisitante")
        self.pushButtonVisitanteRegistradoBuscarSalida = QtWidgets.QPushButton(self.groupBoxIdentificarVisitante)
        self.pushButtonVisitanteRegistradoBuscarSalida.setGeometry(QtCore.QRect(470, 30, 211, 31))
        self.pushButtonVisitanteRegistradoBuscarSalida.setStyleSheet("")
        self.pushButtonVisitanteRegistradoBuscarSalida.setObjectName("pushButtonVisitanteRegistradoBuscarSalida")
        self.lineEditNumIdentificacionBuscarSalida = QtWidgets.QLineEdit(self.groupBoxIdentificarVisitante)
        self.lineEditNumIdentificacionBuscarSalida.setGeometry(QtCore.QRect(220, 30, 241, 31))

        self.lineEditNumIdentificacionBuscarSalida.setObjectName("lineEditNumIdentificacionBuscarSalida")
        self.labelNumeroIdentificacionRegistrarVisita_2 = QtWidgets.QLabel(self.groupBoxIdentificarVisitante)
        self.labelNumeroIdentificacionRegistrarVisita_2.setGeometry(QtCore.QRect(10, 30, 181, 32))
        self.labelNumeroIdentificacionRegistrarVisita_2.setStyleSheet("")
        self.labelNumeroIdentificacionRegistrarVisita_2.setObjectName("labelNumeroIdentificacionRegistrarVisita_2")
        self.labelNombreVisitanteSalida_2 = QtWidgets.QLabel(self.groupBoxIdentificarVisitante)
        self.labelNombreVisitanteSalida_2.setGeometry(QtCore.QRect(10, 120, 181, 21))
        self.labelNombreVisitanteSalida_2.setObjectName("labelNombreVisitanteSalida_2")
        self.labelNombreVisitanteSalida = QtWidgets.QLabel(self.groupBoxIdentificarVisitante)
        self.labelNombreVisitanteSalida.setGeometry(QtCore.QRect(220, 120, 231, 20))
        self.labelNombreVisitanteSalida.setText("")
        self.labelNombreVisitanteSalida.setObjectName("labelNombreVisitanteSalida")
        self.label_5 = QtWidgets.QLabel(self.groupBoxIdentificarVisitante)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 181, 20))
        self.label_5.setObjectName("label_5")
        self.comboBoxTipoIdentificacionBuscarSalida = QtWidgets.QComboBox(self.groupBoxIdentificarVisitante)
        self.comboBoxTipoIdentificacionBuscarSalida.setEnabled(True)
        self.comboBoxTipoIdentificacionBuscarSalida.setGeometry(QtCore.QRect(220, 70, 241, 31))
        self.comboBoxTipoIdentificacionBuscarSalida.setObjectName("comboBoxTipoIdentificacionBuscarSalida")
        self.comboBoxTipoIdentificacionBuscarSalida.addItem("")
        self.comboBoxTipoIdentificacionBuscarSalida.addItem("")
        self.comboBoxTipoIdentificacionBuscarSalida.addItem("")
        self.comboBoxTipoIdentificacionBuscarSalida.addItem("")
        self.comboBoxTipoIdentificacionBuscarSalida.addItem("")
        self.labelAnotacionesSalida = QtWidgets.QLabel(self.groupBoxIdentificarVisitante)
        self.labelAnotacionesSalida.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.labelAnotacionesSalida.setObjectName("labelAnotacionesSalida")
        self.plainTextEditNotasSalida = QtWidgets.QPlainTextEdit(self.groupBoxIdentificarVisitante)
        self.plainTextEditNotasSalida.setGeometry(QtCore.QRect(220, 180, 241, 61))
        self.plainTextEditNotasSalida.setObjectName("plainTextEditNotasSalida")
        self.pushButtonRegistrarSalidaData = QtWidgets.QPushButton(self.groupBoxIdentificarVisitante)
        self.pushButtonRegistrarSalidaData.setGeometry(QtCore.QRect(220, 270, 241, 31))
        self.pushButtonRegistrarSalidaData.setObjectName("pushButtonRegistrarSalidaData")
        self.tab_widget.addTab(self.tabRegistroSalida, "")
        self.tab_widget.setStyleSheet(open( get_path_file(__file__,['css','hide-tabs-style.css'])).read())
        self.retranslateUiSalida()


    def retranslateUiSalida(self):

        _translate = QtCore.QCoreApplication.translate

        self.groupBoxDatosVisitaSalida.setTitle(_translate("Dialog", "Datos de la visita"))
        self.groupBoxIdentificarVisitante.setTitle(_translate("Dialog", "Identificar visitante"))
        self.pushButtonVisitanteRegistradoBuscarSalida.setText(_translate("Dialog", "Buscar"))
        self.labelNumeroIdentificacionRegistrarVisita_2.setText(_translate("Dialog", "Número de identificación "))
        self.labelNombreVisitanteSalida_2.setText(_translate("Dialog", "Nombre"))
        self.label_5.setText(_translate("Dialog", "Tipo de identificación"))
        self.comboBoxTipoIdentificacionBuscarSalida.setItemText(0, _translate("Dialog", "CC"))
        self.comboBoxTipoIdentificacionBuscarSalida.setItemText(1, _translate("Dialog", "DNI"))
        self.comboBoxTipoIdentificacionBuscarSalida.setItemText(2, _translate("Dialog", "TI"))
        self.comboBoxTipoIdentificacionBuscarSalida.setItemText(3, _translate("Dialog", "TP"))
        self.comboBoxTipoIdentificacionBuscarSalida.setItemText(4, _translate("Dialog", "RC"))
        self.labelAnotacionesSalida.setText(_translate("Dialog", "Anotaciones "))
        self.pushButtonRegistrarSalidaData.setText(_translate("Dialog", "Registrar salida"))




    def set_view_estado_dispositivo(self):
        self.tab_widget.setCurrentIndex(2)

    def load_default_values(self):
        self.main_controller.set_default_values()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ph_window = QtWidgets.QMainWindow()
    ui = MainPHWindow()
    ui.setupUi(main_ph_window)
    main_ph_window.show()
    sys.exit(app.exec_())
