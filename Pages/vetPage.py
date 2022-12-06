# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vet_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VetWindow(object):
    def setupUi(self, VetWindow):
        VetWindow.setObjectName("VetWindow")
        VetWindow.resize(896, 622)
        VetWindow.setStyleSheet("background: #23B7C8;")
        self.centralwidget = QtWidgets.QWidget(VetWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vetTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.vetTabs.setGeometry(QtCore.QRect(0, 0, 896, 622))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vetTabs.setFont(font)
        self.vetTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.vetTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.vetTabs.setElideMode(QtCore.Qt.ElideNone)
        self.vetTabs.setObjectName("vetTabs")
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        self.label_2 = QtWidgets.QLabel(self.searchTab)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 411, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("media/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.searchTab)
        self.label_3.setGeometry(QtCore.QRect(380, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.searchPetField = QtWidgets.QLineEdit(self.searchTab)
        self.searchPetField.setGeometry(QtCore.QRect(300, 370, 251, 31))
        self.searchPetField.setStyleSheet("background: white;")
        self.searchPetField.setObjectName("searchPetField")
        self.searchPetButton = QtWidgets.QPushButton(self.searchTab)
        self.searchPetButton.setGeometry(QtCore.QRect(560, 370, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchPetButton.setFont(font)
        self.searchPetButton.setStyleSheet("background: #1CD050;\n"
"color: white;")
        self.searchPetButton.setObjectName("searchPetButton")
        self.petInfoWidget = QtWidgets.QWidget(self.searchTab)
        self.petInfoWidget.setGeometry(QtCore.QRect(0, 0, 896, 591))
        self.petInfoWidget.setObjectName("petInfoWidget")
        self.petListWidget1 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget1.setGeometry(QtCore.QRect(100, 40, 241, 501))
        self.petListWidget1.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget1.setObjectName("petListWidget1")
        self.petInfoBackButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.petInfoBackButton.setFont(font)
        self.petInfoBackButton.setStyleSheet("background: #03e8fc;")
        self.petInfoBackButton.setObjectName("petInfoBackButton")
        self.petListWidget2 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget2.setGeometry(QtCore.QRect(370, 40, 481, 231))
        self.petListWidget2.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget2.setObjectName("petListWidget2")
        self.petListWidget3 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget3.setGeometry(QtCore.QRect(370, 310, 481, 231))
        self.petListWidget3.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget3.setObjectName("petListWidget3")
        self.vetTabs.addTab(self.searchTab, "")
        self.myAppointmentsTab = QtWidgets.QWidget()
        self.myAppointmentsTab.setObjectName("myAppointmentsTab")
        self.label = QtWidgets.QLabel(self.myAppointmentsTab)
        self.label.setGeometry(QtCore.QRect(60, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.myAppointmentsTable = QtWidgets.QTableWidget(self.myAppointmentsTab)
        self.myAppointmentsTable.setGeometry(QtCore.QRect(60, 90, 781, 461))
        self.myAppointmentsTable.setStyleSheet("background: white;\n"
"border: 4px solid black;")
        self.myAppointmentsTable.setObjectName("myAppointmentsTable")
        self.myAppointmentsTable.setColumnCount(0)
        self.myAppointmentsTable.setRowCount(0)
        self.createAppointmentTable = QtWidgets.QPushButton(self.myAppointmentsTab)
        self.createAppointmentTable.setGeometry(QtCore.QRect(672, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.createAppointmentTable.setFont(font)
        self.createAppointmentTable.setStyleSheet("background: #1CD050;\n"
"color: white;")
        self.createAppointmentTable.setObjectName("createAppointmentTable")
        self.vetTabs.addTab(self.myAppointmentsTab, "")
        VetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VetWindow)
        self.vetTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VetWindow)

    def retranslateUi(self, VetWindow):
        _translate = QtCore.QCoreApplication.translate
        VetWindow.setWindowTitle(_translate("VetWindow", "e-Pet"))
        self.label_3.setText(_translate("VetWindow", "Search Pet"))
        self.searchPetButton.setText(_translate("VetWindow", "Find"))
        self.petInfoBackButton.setText(_translate("VetWindow", "Back"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(self.searchTab), _translate("VetWindow", "Search"))
        self.label.setText(_translate("VetWindow", "My Appointments"))
        self.createAppointmentTable.setText(_translate("VetWindow", "Create Appointment"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(self.myAppointmentsTab), _translate("VetWindow", "My Appointments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VetWindow = QtWidgets.QMainWindow()
    ui = Ui_VetWindow()
    ui.setupUi(VetWindow)
    VetWindow.show()
    sys.exit(app.exec_())

