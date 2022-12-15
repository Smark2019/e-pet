# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_vaccination_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addVaccinationWindow(object):
    def setupUi(self, addVaccinationWindow):
        addVaccinationWindow.setObjectName("addVaccinationWindow")
        addVaccinationWindow.resize(651, 288)
        addVaccinationWindow.setMinimumSize(QtCore.QSize(700, 320))
        addVaccinationWindow.setMaximumSize(QtCore.QSize(700, 320))
        addVaccinationWindow.setStyleSheet("background: #23B7C8;")
        addVaccinationWindow.setWindowIcon(QtGui.QIcon('media/logo.png'))
        self.centralwidget = QtWidgets.QWidget(addVaccinationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(75, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(95, 170, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(175, 212, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.vaccinationNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.vaccinationNameField.setGeometry(QtCore.QRect(240, 90, 361, 22))
        self.vaccinationNameField.setStyleSheet("background: white;")
        self.vaccinationNameField.setObjectName("vaccinationNameField")
        self.dateOfVaccinationField = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateOfVaccinationField.setGeometry(QtCore.QRect(240, 130, 361, 22))
        self.dateOfVaccinationField.setStyleSheet("background: white;")
        self.dateOfVaccinationField.setAlignment(QtCore.Qt.AlignCenter)
        self.dateOfVaccinationField.setCalendarPopup(True)
        self.dateOfVaccinationField.setObjectName("dateOfVaccinationField")
        self.vaccinationCountField = QtWidgets.QSpinBox(self.centralwidget)
        self.vaccinationCountField.setGeometry(QtCore.QRect(240, 210, 361, 22))
        self.vaccinationCountField.setStyleSheet("background: white;")
        self.vaccinationCountField.setAlignment(QtCore.Qt.AlignCenter)
        self.vaccinationCountField.setObjectName("vaccinationCountField")
        self.vaccinationDoseGivenField = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.vaccinationDoseGivenField.setGeometry(QtCore.QRect(240, 170, 361, 22))
        self.vaccinationDoseGivenField.setStyleSheet("background: white;")
        self.vaccinationDoseGivenField.setFrame(False)
        self.vaccinationDoseGivenField.setAlignment(QtCore.Qt.AlignCenter)
        self.vaccinationDoseGivenField.setObjectName("vaccinationDoseGivenField")
        self.saveVaccinationButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveVaccinationButton.setGeometry(QtCore.QRect(510, 250, 93, 28))
        self.saveVaccinationButton.setStyleSheet("background: #1CD050;")
        self.saveVaccinationButton.setObjectName("saveVaccinationButton")


        addVaccinationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addVaccinationWindow)
        QtCore.QMetaObject.connectSlotsByName(addVaccinationWindow)

    def retranslateUi(self, addVaccinationWindow):
        _translate = QtCore.QCoreApplication.translate
        addVaccinationWindow.setWindowTitle(_translate("addVaccinationWindow", "e-Pet - Add Vaccination"))
        self.label.setText(_translate("addVaccinationWindow", "Add Vaccination"))
        self.label_2.setText(_translate("addVaccinationWindow", "Vaccinaton Name:"))
        self.label_3.setText(_translate("addVaccinationWindow", "Date of Vaccination:"))
        self.label_4.setText(_translate("addVaccinationWindow", "Dose Given (mg):"))
        self.label_5.setText(_translate("addVaccinationWindow", "Count:"))
        self.saveVaccinationButton.setText(_translate("addVaccinationWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addVaccinationWindow = QtWidgets.QMainWindow()
    ui = Ui_addVaccinationWindow()
    ui.setupUi(addVaccinationWindow)
    addVaccinationWindow.show()
    sys.exit(app.exec_())

