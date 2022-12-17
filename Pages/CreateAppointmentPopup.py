# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_appointment_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createAppointmentWindow(object):
    def setupUi(self, createAppointmentWindow):
        createAppointmentWindow.setObjectName("createAppointmentWindow")
        createAppointmentWindow.resize(651, 330)
        createAppointmentWindow.setMinimumSize(QtCore.QSize(651, 330))
        createAppointmentWindow.setMaximumSize(QtCore.QSize(651, 330))
        createAppointmentWindow.setStyleSheet("background: #23B7C8;")
        createAppointmentWindow.setWindowIcon(QtGui.QIcon('media/logo.png'))
        self.centralwidget = QtWidgets.QWidget(createAppointmentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(172, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(63, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.petIDField = QtWidgets.QLineEdit(self.centralwidget)
        self.petIDField.setGeometry(QtCore.QRect(240, 90, 371, 22))
        self.petIDField.setStyleSheet("background: white;")
        self.petIDField.setObjectName("petIDField")
        self.dateOfAppointmentField = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateOfAppointmentField.setGeometry(QtCore.QRect(240, 130, 371, 22))
        self.dateOfAppointmentField.setStyleSheet("background: white;")
        self.dateOfAppointmentField.setAlignment(QtCore.Qt.AlignCenter)
        self.dateOfAppointmentField.setCalendarPopup(True)
        self.dateOfAppointmentField.setObjectName("dateOfAppointmentField")
        self.saveAppointmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveAppointmentButton.setGeometry(QtCore.QRect(520, 260, 93, 28))
        self.saveAppointmentButton.setStyleSheet("background: #1CD050;")
        self.saveAppointmentButton.setObjectName("saveAppointmentButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(82, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.appointmentTypeField = QtWidgets.QComboBox(self.centralwidget)
        self.appointmentTypeField.setGeometry(QtCore.QRect(240, 170, 371, 22))
        self.appointmentTypeField.setStyleSheet("background: white;")
        self.appointmentTypeField.setObjectName("appointmentTypeField")
        self.appointmentTypeField.addItem("")
        self.appointmentTypeField.setItemText(0, "")
        self.appointmentTypeField.addItem("")
        self.appointmentTypeField.addItem("")
        self.appointmentTypeField.addItem("")
        self.appointmentTypeField.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(132, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.vaccinationField = QtWidgets.QLineEdit(self.centralwidget)
        self.vaccinationField.setEnabled(False)
        
        self.vaccinationField.setGeometry(QtCore.QRect(240, 210, 371, 22))
        self.vaccinationField.setStyleSheet("background: white;")
        self.vaccinationField.setPlaceholderText("")
        self.vaccinationField.setObjectName("vaccinationField")
        createAppointmentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(createAppointmentWindow)
        QtCore.QMetaObject.connectSlotsByName(createAppointmentWindow)

    def retranslateUi(self, createAppointmentWindow):
        _translate = QtCore.QCoreApplication.translate
        createAppointmentWindow.setWindowTitle(_translate("createAppointmentWindow", "e-Pet - Create Appointment"))
        self.label.setText(_translate("createAppointmentWindow", "Create Appointment"))
        self.label_2.setText(_translate("createAppointmentWindow", "Pet ID:"))
        self.label_3.setText(_translate("createAppointmentWindow", "Date of Appointment:"))
        self.saveAppointmentButton.setText(_translate("createAppointmentWindow", "Save"))
        self.label_4.setText(_translate("createAppointmentWindow", "Appointment Type:"))
        self.appointmentTypeField.setItemText(1, _translate("createAppointmentWindow", "Checkup"))
        self.appointmentTypeField.setItemText(2, _translate("createAppointmentWindow", "Surgery"))
        self.appointmentTypeField.setItemText(3, _translate("createAppointmentWindow", "Vaccination"))
        self.appointmentTypeField.setItemText(4, _translate("createAppointmentWindow", "Other"))
        self.label_5.setText(_translate("createAppointmentWindow", "Vaccination:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createAppointmentWindow = QtWidgets.QMainWindow()
    ui = Ui_createAppointmentWindow()
    ui.setupUi(createAppointmentWindow)
    createAppointmentWindow.show()
    sys.exit(app.exec_())

