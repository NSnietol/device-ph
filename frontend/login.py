# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import QMessageBox, QInputDialog, QDesktopWidget
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
import os



class LoginForm():
    def setupUi(self, Dialog, controller):
        self.controller = controller
        self.Dialog = Dialog
        self.Dialog.setObjectName("Login")
        self.Dialog.resize(452, 551)
        path_d = os.path.join(self.get_path(),'css','style.css')
        self.Dialog.setStyleSheet(open(path_d).read())
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 80, 491, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 70, 301, 81))
        self.label.setText("")
        path_d = os.path.join(self.get_path(),'media','asset-log-official.png')
        self.label.setPixmap(QtGui.QPixmap(path_d))
        self.label.setObjectName("label")
        self.push_button_iniciar_sesion = QtWidgets.QPushButton(self.frame)
        self.push_button_iniciar_sesion.setGeometry(
            QtCore.QRect(120, 340, 241, 41))
        self.push_button_iniciar_sesion.setObjectName("push_button_iniciar_sesion")
        self.line_edit_usuario = QtWidgets.QLineEdit(self.frame)
        self.line_edit_usuario.setGeometry(QtCore.QRect(50, 170, 351, 51))
        self.line_edit_usuario.setObjectName("line_edit_usuario")
        self.line_edit_password = QtWidgets.QLineEdit(self.frame)
        self.line_edit_password.setGeometry(QtCore.QRect(50, 250, 351, 51))
        self.line_edit_password.setText("")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(160, 30, 131, 121))
        self.toolButton.setText("")

        icon = QtGui.QIcon()
        path_d = os.path.join(self.get_path(),'media','login.png')
        icon.addPixmap(QtGui.QPixmap(path_d),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(120, 80))
        self.toolButton.setAutoExclusive(False)
        self.toolButton.setObjectName("toolButton")

        self._create_events()
        self.Dialog.setFixedSize(self.Dialog.size())

        self.center()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.push_button_iniciar_sesion.setText(_translate("Dialog", "Iniciar"))
        self.line_edit_usuario.setPlaceholderText(
            _translate("Dialog", "Usuario"))
        self.line_edit_password.setPlaceholderText(
            _translate("Dialog", "Contraseña"))

    def center(self):
        q_rect = self.Dialog.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        q_rect.moveCenter(center_point)
        self.Dialog.move(q_rect.topLeft())

    def showMain(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.main = Ui_MainWindow()
        self.main.setupUi(self.MainWindow)
        self.MainWindow.show()

    def _create_events(self):
        self.line_edit_password.returnPressed.connect(self.get_functions)
        self.push_button_iniciar_sesion.clicked.connect(self.get_functions)

    def get_path(self):
        return os.path.dirname(__file__)
    
    def get_functions(self):
        return self.controller.login_sgph()

   



if __name__ == "__main__":
    import sys

 
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoginForm()
    ui.setupUi(Dialog, None)
    Dialog.show()
    sys.exit(app.exec_())
