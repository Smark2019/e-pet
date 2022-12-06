# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(591, 345)
        LoginWindow.setMinimumSize(QtCore.QSize(591, 345))
        LoginWindow.setMaximumSize(QtCore.QSize(591, 345))
        LoginWindow.setStyleSheet("background: #23B7C8;")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.idField = QtWidgets.QLineEdit(self.centralwidget)
        self.idField.setGeometry(QtCore.QRect(160, 170, 381, 21))
        self.idField.setStyleSheet("background: white;")
        self.idField.setObjectName("idField")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 212, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(255, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background: #1CD050;\n"
"color: white;")
        self.loginButton.setObjectName("loginButton")
        self.passField = QtWidgets.QLineEdit(self.centralwidget)
        self.passField.setGeometry(QtCore.QRect(160, 212, 381, 21))
        self.passField.setStyleSheet("background: white;")
        self.passField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passField.setObjectName("passField")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 167, 21, 21))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("media/avatar.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(37, 210, 21, 21))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("media/lock.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.showPass = QtWidgets.QCheckBox(self.centralwidget)
        self.showPass.setGeometry(QtCore.QRect(160, 240, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.showPass.setFont(font)
        self.showPass.setObjectName("showPass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(155, 20, 281, 141))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("media/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "e-Pet"))
        self.label.setText(_translate("LoginWindow", "User ID:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))
        self.loginButton.setText(_translate("LoginWindow", "Log In"))
        self.showPass.setText(_translate("LoginWindow", "Show Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

