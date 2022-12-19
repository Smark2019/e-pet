# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_allergy_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addAllergyWindow(object):
    def setupUi(self, addAllergyWindow):
        addAllergyWindow.setObjectName("addAllergyWindow")
        addAllergyWindow.resize(651, 394)
        addAllergyWindow.setMinimumSize(QtCore.QSize(651, 394))
        addAllergyWindow.setMaximumSize(QtCore.QSize(651, 394))
        addAllergyWindow.setStyleSheet("background: #23B7C8;")
        addAllergyWindow.setWindowIcon(QtGui.QIcon('media/logo.png'))
        self.centralwidget = QtWidgets.QWidget(addAllergyWindow)
        self.centralwidget.setObjectName("centralwidget")
        #label added into centralwidget.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #label_2 added into centralwidget.
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(171, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #allergyDrugsField added into centralwidget.
        self.allergyDrugsField = QtWidgets.QLineEdit(self.centralwidget)
        self.allergyDrugsField.setGeometry(QtCore.QRect(240, 90, 371, 22))
        self.allergyDrugsField.setStyleSheet("background: white;")
        self.allergyDrugsField.setObjectName("allergyDrugsField")
        #saveAllergyButton added into centralwidget.
        self.saveAllergyButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveAllergyButton.setGeometry(QtCore.QRect(520, 340, 93, 28))
        self.saveAllergyButton.setStyleSheet("background: #1CD050;")
        self.saveAllergyButton.setObjectName("saveAllergyButton")
        #label_4 added into centralwidget.
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(132, 125, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #allergyDescriptionField added into centralwidget.
        self.allergyDescriptionField = QtWidgets.QTextEdit(self.centralwidget)
        self.allergyDescriptionField.setGeometry(QtCore.QRect(240, 130, 371, 191))
        self.allergyDescriptionField.setStyleSheet("background: white;")
        self.allergyDescriptionField.setObjectName("allergyDescriptionField")
        addAllergyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addAllergyWindow)
        QtCore.QMetaObject.connectSlotsByName(addAllergyWindow)

    def retranslateUi(self, addAllergyWindow):
        _translate = QtCore.QCoreApplication.translate
        addAllergyWindow.setWindowTitle(_translate("addAllergyWindow", "e-Pet - Add Allergy"))
        self.label.setText(_translate("addAllergyWindow", "Add Allergy"))
        self.label_2.setText(_translate("addAllergyWindow", "Drugs:"))
        self.saveAllergyButton.setText(_translate("addAllergyWindow", "Save"))
        self.label_4.setText(_translate("addAllergyWindow", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addAllergyWindow = QtWidgets.QMainWindow()
    ui = Ui_addAllergyWindow()
    ui.setupUi(addAllergyWindow)
    addAllergyWindow.show()
    sys.exit(app.exec_())

