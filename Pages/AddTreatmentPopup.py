# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_treatment_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addTreatmentWindow(object):
    def setupUi(self, addTreatmentWindow):
        addTreatmentWindow.setObjectName("addTreatmentWindow")
        addTreatmentWindow.resize(651, 394)
        addTreatmentWindow.setMinimumSize(QtCore.QSize(651, 394))
        addTreatmentWindow.setMaximumSize(QtCore.QSize(651, 394))
        addTreatmentWindow.setStyleSheet("background: #23B7C8;")
        addTreatmentWindow.setWindowIcon(QtGui.QIcon('media/logo.png'))
        self.centralwidget = QtWidgets.QWidget(addTreatmentWindow)
        self.centralwidget.setObjectName("centralwidget")
        #label added into centralwidget.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #label_2 added into central widget.
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(112, 90, 115, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #label_3 added into centralwidget.
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.treatmentUsedMedicineField = QtWidgets.QLineEdit(self.centralwidget)
        self.treatmentUsedMedicineField.setGeometry(QtCore.QRect(240, 90, 371, 22))
        self.treatmentUsedMedicineField.setStyleSheet("background: white;")
        self.treatmentUsedMedicineField.setObjectName("treatmentUsedMedicineField")
        self.dateOfTreatmentField = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateOfTreatmentField.setGeometry(QtCore.QRect(240, 130, 371, 22))
        self.dateOfTreatmentField.setStyleSheet("background: white;")
        self.dateOfTreatmentField.setAlignment(QtCore.Qt.AlignCenter)
        self.dateOfTreatmentField.setCalendarPopup(True)
        self.dateOfTreatmentField.setObjectName("dateOfTreatmentField")
        self.saveTreatmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveTreatmentButton.setGeometry(QtCore.QRect(520, 340, 93, 28))
        self.saveTreatmentButton.setStyleSheet("background: #1CD050;")
        self.saveTreatmentButton.setObjectName("saveTreatmentButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(132, 165, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.treatmentDescriptionField = QtWidgets.QTextEdit(self.centralwidget)
        self.treatmentDescriptionField.setGeometry(QtCore.QRect(240, 170, 371, 151))
        self.treatmentDescriptionField.setStyleSheet("background: white;")
        self.treatmentDescriptionField.setObjectName("treatmentDescriptionField")
        addTreatmentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addTreatmentWindow)
        QtCore.QMetaObject.connectSlotsByName(addTreatmentWindow)

    def retranslateUi(self, addTreatmentWindow):
        _translate = QtCore.QCoreApplication.translate
        addTreatmentWindow.setWindowTitle(_translate("addTreatmentWindow", "e-Pet - Add Treatment"))
        self.label.setText(_translate("addTreatmentWindow", "Add Treatment"))
        self.label_2.setText(_translate("addTreatmentWindow", "Used Medicine:"))
        self.label_3.setText(_translate("addTreatmentWindow", "Date of Treatment:"))
        self.saveTreatmentButton.setText(_translate("addTreatmentWindow", "Save"))
        self.label_4.setText(_translate("addTreatmentWindow", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTreatmentWindow = QtWidgets.QMainWindow()
    ui = Ui_addTreatmentWindow()
    ui.setupUi(addTreatmentWindow)
    addTreatmentWindow.show()
    sys.exit(app.exec_())

