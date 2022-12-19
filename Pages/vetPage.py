# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vet_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from .AddVaccinationPopup  import *
from .AddTreatmentPopup import *
from .AddAllergyPopup import *
from .CreateAppointmentPopup import *

class Ui_VetWindow(object):

    def openCreatAppointmentPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.popUi = Ui_createAppointmentWindow()
        self.popUi.setupUi(self.window)
        self.window.show()


    def openAddVaccinationPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.popUi = Ui_addVaccinationWindow()
        self.popUi.setupUi(self.window)
        self.window.show()

    def openAddTreatmentPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.popUi = Ui_addTreatmentWindow()
        self.popUi.setupUi(self.window)
        self.window.show()

    def openAddAllergyPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.popUi = Ui_addAllergyWindow()
        self.popUi.setupUi(self.window)
        self.window.show()

    def setupUi(self, VetWindow):
        self.popUi = Ui_addVaccinationWindow()  # only for start case
        VetWindow.setObjectName("VetWindow")
        VetWindow.setWindowIcon(QtGui.QIcon('media/logo.png'))
        # vetWindow size defined.
        VetWindow.resize(896, 622)
        VetWindow.setStyleSheet("background: #23B7C8;")
        # central widget added into vetWindow.
        self.centralwidget = QtWidgets.QWidget(VetWindow)
        self.centralwidget.setObjectName("centralwidget")
        # vetTabs added into centralwidget.
        self.vetTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.vetTabs.setGeometry(QtCore.QRect(0, 0, 896, 622))
        font = QtGui.QFont()
        # font size defined.
        font.setPointSize(10)
        self.vetTabs.setFont(font)
        self.vetTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.vetTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.vetTabs.setElideMode(QtCore.Qt.ElideNone)
        self.vetTabs.setObjectName("vetTabs")
        # searchTab created and editted.
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        # label2 added into searchTable.
        self.label_2 = QtWidgets.QLabel(self.searchTab)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 411, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("media/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        #label_3 added into searchTab.
        self.label_3 = QtWidgets.QLabel(self.searchTab)
        self.label_3.setGeometry(QtCore.QRect(380, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #searchPetField added into searchTab.
        self.searchPetField = QtWidgets.QLineEdit(self.searchTab)
        self.searchPetField.setGeometry(QtCore.QRect(300, 370, 251, 31))
        self.searchPetField.setStyleSheet("background: white;")
        self.searchPetField.setObjectName("searchPetField")
        #searchPetButton added into searchTab.
        self.searchPetButton = QtWidgets.QPushButton(self.searchTab)
        self.searchPetButton.setGeometry(QtCore.QRect(560, 370, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchPetButton.setFont(font)
        self.searchPetButton.setStyleSheet("background: #1CD050;\n"
                                           "color: white;")
        self.searchPetButton.setObjectName("searchPetButton")
        

        #addPetButton added into searchTab.
        self.addPetButton = QtWidgets.QPushButton(self.searchTab)
        self.addPetButton.setGeometry(QtCore.QRect(350, 530, 196, 31))
        #font editted.
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addPetButton.setFont(font)
        self.addPetButton.setStyleSheet("background: orange;\n"
                                        "color: white;")
        self.addPetButton.setObjectName("addPetButton")

#########################################################################################################
#                                       ADD PET WIDGET                                                  #
#########################################################################################################
        # below shows the editable pet info page to add new pets to db
        self.addPetWidget = QtWidgets.QWidget(self.searchTab)
        self.addPetWidget.setGeometry(QtCore.QRect(0, 0, 896, 591))
        self.addPetWidget.setObjectName("addPetWidget")

        # this is the "back" button to go back to the search page.
        self.addPetBackButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetBackButton.setFont(font)
        self.addPetBackButton.setStyleSheet("background: #03e8fc;")
        self.addPetBackButton.setObjectName("addPetBackButton")

        # this is the "save" button.
        self.addPetSaveButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetSaveButton.setGeometry(QtCore.QRect(220, 450, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addPetSaveButton.setFont(font)
        self.addPetSaveButton.setStyleSheet(
            "background: #1CD050; border-radius: 5px;")
        self.addPetSaveButton.setObjectName("addPetSaveButton")

        # below is the field to enter the "name" attribute of the "pet" table of the db
        self.addPetNameField = QtWidgets.QLineEdit(self.addPetWidget)
        self.addPetNameField.setGeometry(QtCore.QRect(300, 95, 400, 22))
        self.addPetNameField.setStyleSheet("background: white;")
        self.addPetNameField.setObjectName("addPetNameField")
        self.addPetNameLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetNameLabel.setGeometry(QtCore.QRect(215, 95, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetNameLabel.setFont(font)
        self.addPetNameLabel.setObjectName("addPetNameLabel")

        # below is the field to enter the "date_of_birth" attribute of the "pet" table of the db
        self.addPetDateOfBirthField = QtWidgets.QDateTimeEdit(
            self.addPetWidget)
        self.addPetDateOfBirthField.setGeometry(QtCore.QRect(300, 137, 400, 22))
        self.addPetDateOfBirthField.setStyleSheet("background: white;")
        self.addPetDateOfBirthField.setAlignment(QtCore.Qt.AlignCenter)
        self.addPetDateOfBirthField.setCalendarPopup(True)
        self.addPetDateOfBirthField.setObjectName("addPetdateOfBirthField")
        self.addPetDateOfBirthLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetDateOfBirthLabel.setGeometry(QtCore.QRect(190, 137, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetDateOfBirthLabel.setFont(font)
        self.addPetDateOfBirthLabel.setObjectName("addPetdateOfBirthLabel")

        # below is the field to enter the "species" attribute of the "pet" table of the db
        self.addPetSpeciesField = QtWidgets.QComboBox(self.addPetWidget)
        self.addPetSpeciesField.setGeometry(QtCore.QRect(300, 181, 400, 22))
        self.addPetSpeciesField.addItems(
            ["", "Dog", "Cat", "Bird", "Rabbit", "Hamster", "Guinea Pig", "Ferret"])
        self.addPetSpeciesField.setStyleSheet("background: white;")
        self.addPetSpeciesField.setObjectName("addPetSpeciesField")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addPetSpeciesField.setFont(font)
        self.addPetSpeciesLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetSpeciesLabel.setGeometry(QtCore.QRect(230, 181, 60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetSpeciesLabel.setFont(font)
        self.addPetSpeciesLabel.setObjectName("addPetSpeciesLabel")

        # below is the field to enter the "gender" attribute of the "pet" table of the db
        self.addPetMaleRadioButton = QtWidgets.QRadioButton(self.addPetWidget)
        self.addPetMaleRadioButton.setGeometry(QtCore.QRect(320, 225, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetMaleRadioButton.setFont(font)
        self.addPetMaleRadioButton.setObjectName("addPetMaleRadioButton")
        self.addPetFemaleRadioButton = QtWidgets.QRadioButton(self.addPetWidget)
        self.addPetFemaleRadioButton.setGeometry(QtCore.QRect(400, 225, 100, 22))
        self.addPetFemaleRadioButton.setFont(font)
        self.addPetFemaleRadioButton.setObjectName("addPetFemaleRadioButton")
        self.addPetGenderLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetGenderLabel.setGeometry(QtCore.QRect(233, 225, 60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetGenderLabel.setFont(font)
        self.addPetGenderLabel.setObjectName("addPetGenderLabel")

        # below is the field to enter the "sterility" attribute of the "pet" table of the db
        self.addPetSterilityField = QtWidgets.QCheckBox(self.addPetWidget)
        self.addPetSterilityField.setGeometry(QtCore.QRect(320, 269, 200, 22))
        self.addPetSterilityField.setObjectName("addPetSterilityField")
        self.addPetSterilityLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetSterilityLabel.setGeometry(QtCore.QRect(240, 269, 60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetSterilityLabel.setFont(font)
        self.addPetSterilityLabel.setObjectName("addPetSterilityLabel")

        # below is the field to enter the "health_status" attribute of the "pet" table of the db
        self.addPetHealthField = QtWidgets.QComboBox(self.addPetWidget)
        self.addPetHealthField.setGeometry(QtCore.QRect(300, 313, 400, 22))
        self.addPetHealthField.addItems(["", "Healthy", "Sick", "Injured"])
        self.addPetHealthField.setStyleSheet("background: white;")
        self.addPetHealthField.setObjectName("addPetHealthField")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addPetHealthField.setFont(font)
        self.addPetHealthLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetHealthLabel.setGeometry(QtCore.QRect(185, 313, 105, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetHealthLabel.setFont(font)
        self.addPetHealthLabel.setObjectName("addPetHealthLabel")

        # below is the field to enter the "owner_ID" attribute of the "pet" table of the db
        self.addPetOwnerIDField = QtWidgets.QLineEdit(self.addPetWidget)
        self.addPetOwnerIDField.setGeometry(QtCore.QRect(300, 357, 400, 22))
        self.addPetOwnerIDField.setStyleSheet("background: white;")
        self.addPetOwnerIDField.setObjectName("addPetOwnerIDField")
        self.addPetOwnerIDLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetOwnerIDLabel.setGeometry(QtCore.QRect(215, 357, 75, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetOwnerIDLabel.setFont(font)
        self.addPetOwnerIDLabel.setObjectName("addPetOwnerIDLabel")


#########################################################################################################
#                                       PET INFO WIDGET                                                 #
#########################################################################################################
        # below shows the read-only widget that contains the pet info
        self.petInfoWidget = QtWidgets.QWidget(self.searchTab)
        self.petInfoWidget.setGeometry(QtCore.QRect(0, 0, 896, 591))
        self.petInfoWidget.setObjectName("petInfoWidget")

        # this is the LIST widget on the left side of the screen for "pet" table of the db
        self.petInfoList = QtWidgets.QListWidget(self.petInfoWidget)
        self.petInfoList.setGeometry(QtCore.QRect(100, 40, 241, 300))
        self.petInfoList.setStyleSheet("background:white;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 16pt;")
        self.petInfoList.setObjectName("petInfoList")

        # this is the "back" button to go back to the search page.
        self.petInfoBackButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.petInfoBackButton.setFont(font)
        self.petInfoBackButton.setStyleSheet("background: #03e8fc;")
        self.petInfoBackButton.setObjectName("petInfoBackButton")

        # this is the "add vaccincation" button.
        self.petInfoAddVaccinationButton = QtWidgets.QPushButton(
            self.petInfoWidget, clicked=lambda: self.openAddVaccinationPopup())
        self.petInfoAddVaccinationButton.setGeometry(
            QtCore.QRect(100, 350, 241, 57))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.petInfoAddVaccinationButton.setFont(font)
        self.petInfoAddVaccinationButton.setStyleSheet(
            "background: orange; border-radius: 5px;")
        self.petInfoAddVaccinationButton.setObjectName(
            "petInfoAddVaccinationButton")

        # this is the "add treatment" button.
        self.petInfoAddTreatmentButton = QtWidgets.QPushButton(
            self.petInfoWidget, clicked=lambda: self.openAddTreatmentPopup())
        self.petInfoAddTreatmentButton.setGeometry(
            QtCore.QRect(100, 417, 241, 57))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.petInfoAddTreatmentButton.setFont(font)
        self.petInfoAddTreatmentButton.setStyleSheet(
            "background: orange; border-radius: 5px;")
        self.petInfoAddTreatmentButton.setObjectName(
            "petInfoAddTreatmentButton")

        # this is the "add allergy" button.
        self.petInfoAddAllergyButton = QtWidgets.QPushButton(
            self.petInfoWidget, clicked=lambda: self.openAddAllergyPopup())
        self.petInfoAddAllergyButton.setGeometry(
            QtCore.QRect(100, 484, 241, 57))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.petInfoAddAllergyButton.setFont(font)
        self.petInfoAddAllergyButton.setStyleSheet(
            "background: orange; border-radius: 5px;")
        self.petInfoAddAllergyButton.setObjectName("petInfoAddAllergyButton")

        # this is the TABLE widget on the right first side of the screen for "vaccination" table of the db
        self.petInfoVaccinationTable = QtWidgets.QTableWidget(
            self.petInfoWidget)
        self.petInfoVaccinationTable.setGeometry(
            QtCore.QRect(370, 40, 481, 160))
        self.petInfoVaccinationTable.setStyleSheet("background:white;\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 10px;")
        self.petInfoVaccinationTable.setObjectName("petInfoVaccinationTable")
        self.petInfoVaccinationTable.setColumnCount(5)
        self.petInfoVaccinationTable.setRowCount(50)
        self.petInfoVaccinationTable.setHorizontalHeaderLabels(
            ["Vet ID", "Name", "Date", "Dose", "Count"])
        self.petInfoVaccinationTable.verticalHeader().setVisible(False)
        self.petInfoVaccinationTable.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)  # makes table read-only
        header = self.petInfoVaccinationTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        # this is the TABLE widget on the right second side of the screen for "treatments" table of the db
        self.petInfoTreatmentTable = QtWidgets.QTableWidget(self.petInfoWidget)
        self.petInfoTreatmentTable.setGeometry(
            QtCore.QRect(370, 210, 481, 160))
        self.petInfoTreatmentTable.setStyleSheet("background:white;\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 10px;")
        self.petInfoTreatmentTable.setObjectName("petInfoTreatmentTable")
        self.petInfoTreatmentTable.setColumnCount(4)
        self.petInfoTreatmentTable.setRowCount(50)
        self.petInfoTreatmentTable.setHorizontalHeaderLabels(
            ["Vet ID", "Description", "Medicine", "Date"])
        self.petInfoTreatmentTable.verticalHeader().setVisible(False)
        self.petInfoTreatmentTable.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)  # makes table read-only

        # this is the TABLE widget on the right third side of the screen for "allergies" table of the db
        self.petInfoAllergiesTable = QtWidgets.QTableWidget(self.petInfoWidget)
        self.petInfoAllergiesTable.setGeometry(
            QtCore.QRect(370, 380, 481, 160))
        self.petInfoAllergiesTable.setStyleSheet("background:white;\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 10px;")
        self.petInfoAllergiesTable.setObjectName("petInfoAllergiesTable")
        self.petInfoAllergiesTable.setColumnCount(3)
        self.petInfoAllergiesTable.setRowCount(50)
        self.petInfoAllergiesTable.setHorizontalHeaderLabels(
            ["Vet ID", "Description", "Drugs"])
        self.petInfoAllergiesTable.verticalHeader().setVisible(False)
        self.petInfoAllergiesTable.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)  # makes table read-only
        header = self.petInfoAllergiesTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

#########################################################################################################
#                                       MY APPOINTMENTS WIDGET                                          #
#########################################################################################################

        self.vetTabs.addTab(self.searchTab, "")
        self.myAppointmentsTab = QtWidgets.QWidget()
        self.myAppointmentsTab.setObjectName("myAppointmentsTab")
        self.label = QtWidgets.QLabel(self.myAppointmentsTab)
        self.label.setGeometry(QtCore.QRect(60, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.myAppointmentsTable = QtWidgets.QTableWidget(
            self.myAppointmentsTab)
        self.myAppointmentsTable.setGeometry(QtCore.QRect(60, 90, 781, 461))
        self.myAppointmentsTable.setStyleSheet("background: white;\n"
                                               "border: 4px solid black; border-radius: 10px;")
        self.myAppointmentsTable.setObjectName("myAppointmentsTable")
        self.myAppointmentsTable.setColumnCount(5)
        self.myAppointmentsTable.setRowCount(50)
        self.myAppointmentsTable.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers) # makes read only
        self.myAppointmentsTable.setHorizontalHeaderLabels(
            ["Pet ID", "Vet ID", "Date", "Type", "Vaccination"])
        self.createAppointmentButton = QtWidgets.QPushButton(
            self.myAppointmentsTab, clicked=lambda: self.openCreatAppointmentPopup())
        self.createAppointmentButton.setGeometry(QtCore.QRect(672, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.createAppointmentButton.setFont(font)
        self.createAppointmentButton.setStyleSheet("background: #1CD050;")
        self.createAppointmentButton.setObjectName("createAppointmentButton")
        self.vetTabs.addTab(self.myAppointmentsTab, "")
        VetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VetWindow)
        self.vetTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VetWindow)

        # SETTINGS FOR VISIBILITY OF Widgets:
        self.petInfoWidget.setVisible(False)
        self.addPetWidget.setVisible(False)

    def retranslateUi(self, VetWindow):
        _translate = QtCore.QCoreApplication.translate
        VetWindow.setWindowTitle(_translate("VetWindow", "e-Pet"))
        self.label_3.setText(_translate("VetWindow", "Search Pet"))
        self.searchPetButton.setText(_translate("VetWindow", "Find"))
        self.addPetButton.setText(_translate("VetWindow", "Add Pet"))
        self.addPetBackButton.setText(_translate("VetWindow", "Back"))
        self.addPetNameLabel.setText(_translate("VetWindow", "Pet Name:"))
        self.addPetDateOfBirthLabel.setText(
            _translate("VetWindow", "Date of Birth:"))
        self.addPetSpeciesLabel.setText(_translate("VetWindow", "Species:"))
        self.addPetGenderLabel.setText(_translate("VetWindow", "Gender:"))
        self.addPetMaleRadioButton.setText(_translate("VetWindow", "Male"))
        self.addPetFemaleRadioButton.setText(_translate("VetWindow", "Female"))
        self.addPetSterilityLabel.setText(_translate("VetWindow", "Sterile:"))
        self.addPetHealthLabel.setText(
            _translate("VetWindow", "Health Status:"))
        self.addPetOwnerIDLabel.setText(_translate("VetWindow", "Owner ID:"))
        self.addPetSaveButton.setText(_translate("VetWindow", "Save"))

        self.petInfoBackButton.setText(_translate("VetWindow", "Back"))
        self.petInfoAddVaccinationButton.setText(
            _translate("VetWindow", "Add Vaccination"))
        self.petInfoAddTreatmentButton.setText(
            _translate("VetWindow", "Add Treatment"))
        self.petInfoAddAllergyButton.setText(
            _translate("VetWindow", "Add Allergy"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(
            self.searchTab), _translate("VetWindow", "Search"))
        self.label.setText(_translate("VetWindow", "My Appointments"))
        self.createAppointmentButton.setText(
            _translate("VetWindow", "Create Appointment"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(
            self.myAppointmentsTab), _translate("VetWindow", "My Appointments"))

        self.statusbar = QtWidgets.QStatusBar(VetWindow)
        self.statusbar.setObjectName("statusbar")
        VetWindow.setStatusBar(self.statusbar)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VetWindow = QtWidgets.QMainWindow()
    ui_login = Ui_VetWindow()
    ui_login.setupUi(VetWindow)
    ui_login.label_2.setPixmap(QtGui.QPixmap("../media/logo.png"))

    VetWindow.show()
    sys.exit(app.exec_())
