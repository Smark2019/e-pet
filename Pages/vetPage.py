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
        #vetWindow size defined.
        VetWindow.resize(896, 622)
        VetWindow.setStyleSheet("background: #23B7C8;")
        #central widget added into vetWindow.
        self.centralwidget = QtWidgets.QWidget(VetWindow)
        self.centralwidget.setObjectName("centralwidget")
        #vetTabs added into centralwidget.
        self.vetTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.vetTabs.setGeometry(QtCore.QRect(0, 0, 896, 622))
        font = QtGui.QFont()
        #font size defined.
        font.setPointSize(10)
        self.vetTabs.setFont(font)
        self.vetTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.vetTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.vetTabs.setElideMode(QtCore.Qt.ElideNone)
        self.vetTabs.setObjectName("vetTabs")
         #searchTab created and editted.
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        #label2 added into searchTable.
        self.label_2 = QtWidgets.QLabel(self.searchTab)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 411, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../media/logo.png"))
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
        

        self.addPetButton = QtWidgets.QPushButton(self.searchTab)
        self.addPetButton.setGeometry(QtCore.QRect(350, 530, 196, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addPetButton.setFont(font)
        self.addPetButton.setStyleSheet("background: orange;\n"
"color: white;")
        self.addPetButton.setObjectName("addPetButton")

#########################################################################################################
#                                       ADD PET WIDGET                                                  #
#########################################################################################################
        #below shows the editable pet info page to add new pets to db
        self.addPetWidget = QtWidgets.QWidget(self.searchTab)
        self.addPetWidget.setGeometry(QtCore.QRect(0, 0, 896, 591))
        self.addPetWidget.setObjectName("addPetWidget")
        #this is the "back" button to go back to the search page.
        self.addPetBackButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetBackButton.setFont(font)
        self.addPetBackButton.setStyleSheet("background: #03e8fc;")
        self.addPetBackButton.setObjectName("addPetBackButton")
        #this is the "add vaccincation" button.
        self.addPetAddVaccinationButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetAddVaccinationButton.setGeometry(QtCore.QRect(7, 55, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.addPetAddVaccinationButton.setFont(font)
        self.addPetAddVaccinationButton.setStyleSheet("background: orange;")
        self.addPetAddVaccinationButton.setObjectName("addPetAddVaccinationButton")
        #this is the "add treatment" button.
        self.addPetAddTreatmentButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetAddTreatmentButton.setGeometry(QtCore.QRect(7, 90, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.addPetAddTreatmentButton.setFont(font)
        self.addPetAddTreatmentButton.setStyleSheet("background: orange;")
        self.addPetAddTreatmentButton.setObjectName("addPetAddTreatmentButton")
        #this is the "add allergy" button.
        self.addPetAddAllergyButton = QtWidgets.QPushButton(self.addPetWidget)
        self.addPetAddAllergyButton.setGeometry(QtCore.QRect(7, 125, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.addPetAddAllergyButton.setFont(font)
        self.addPetAddAllergyButton.setStyleSheet("background: orange;")
        self.addPetAddAllergyButton.setObjectName("addPetAddAllergyButton")
        #this is the TABLE widget on the right first side of the screen for "vaccination" table of the db
        self.addPetVaccinationTable = QtWidgets.QTableWidget(self.addPetWidget)
        self.addPetVaccinationTable.setGeometry(QtCore.QRect(450, 40, 400, 160))
        self.addPetVaccinationTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.addPetVaccinationTable.setObjectName("addPetVaccinationTable")
        #this is the TABLE widget on the right second side of the screen for "treatments" table of the db
        self.addPetTreatmentTable = QtWidgets.QTableWidget(self.addPetWidget)
        self.addPetTreatmentTable.setGeometry(QtCore.QRect(450, 210, 400, 160))
        self.addPetTreatmentTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.addPetTreatmentTable.setObjectName("addPetTreatmentTable")
        #this is the TABLE widget on the right third side of the screen for "allergies" table of the db
        self.addPetAllergiesTable = QtWidgets.QTableWidget(self.addPetWidget)
        self.addPetAllergiesTable.setGeometry(QtCore.QRect(450, 380, 400, 160))
        self.addPetAllergiesTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.addPetAllergiesTable.setObjectName("addPetAllergiesTable")
        #below is the field to enter the "name" attribute of the "pet" table of the db
        self.addPetNameField = QtWidgets.QLineEdit(self.addPetWidget)
        self.addPetNameField.setGeometry(QtCore.QRect(230, 45, 200, 22))
        self.addPetNameField.setStyleSheet("background: white;")
        self.addPetNameField.setObjectName("addPetNameField")
        self.addPetNameLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetNameLabel.setGeometry(QtCore.QRect(150, 45, 75, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetNameLabel.setFont(font)
        self.addPetNameLabel.setObjectName("addPetNameLabel")
        #below is the field to enter the "date_of_birth" attribute of the "pet" table of the db
        self.addPetdateOfBirthField = QtWidgets.QDateTimeEdit(self.addPetWidget)
        self.addPetdateOfBirthField.setGeometry(QtCore.QRect(230, 77, 200, 22))
        self.addPetdateOfBirthField.setStyleSheet("background: white;")
        self.addPetdateOfBirthField.setAlignment(QtCore.Qt.AlignCenter)
        self.addPetdateOfBirthField.setCalendarPopup(True)
        self.addPetdateOfBirthField.setObjectName("addPetdateOfBirthField")
        self.addPetdateOfBirthLabel = QtWidgets.QLabel(self.addPetWidget)
        self.addPetdateOfBirthLabel.setGeometry(QtCore.QRect(125, 77, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPetdateOfBirthLabel.setFont(font)
        self.addPetdateOfBirthLabel.setObjectName("addPetdateOfBirthLabel")
        


        #TODO: species, and rest will be added


#########################################################################################################
#                                       PET INFO WIDGET                                                 #
#########################################################################################################
        #below shows the read-only widget that contains the pet info
        self.petInfoWidget = QtWidgets.QWidget(self.searchTab)
        self.petInfoWidget.setGeometry(QtCore.QRect(0, 0, 896, 591))
        self.petInfoWidget.setObjectName("petInfoWidget")
        #this is the LIST widget on the left side of the screen for "pet" table of the db
        self.petInfoList = QtWidgets.QListWidget(self.petInfoWidget)
        self.petInfoList.setGeometry(QtCore.QRect(100, 40, 241, 501))
        self.petInfoList.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petInfoList.setObjectName("petInfoList")
        #this is the "back" button to go back to the search page.
        self.petInfoBackButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.petInfoBackButton.setFont(font)
        self.petInfoBackButton.setStyleSheet("background: #03e8fc;")
        self.petInfoBackButton.setObjectName("petInfoBackButton")
        #this is the "add vaccincation" button.
        self.petInfoAddVaccinationButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoAddVaccinationButton.setGeometry(QtCore.QRect(7, 55, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.petInfoAddVaccinationButton.setFont(font)
        self.petInfoAddVaccinationButton.setStyleSheet("background: orange;")
        self.petInfoAddVaccinationButton.setObjectName("petInfoAddVaccinationButton")
        #this is the "add treatment" button.
        self.petInfoAddTreatmentButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoAddTreatmentButton.setGeometry(QtCore.QRect(7, 90, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.petInfoAddTreatmentButton.setFont(font)
        self.petInfoAddTreatmentButton.setStyleSheet("background: orange;")
        self.petInfoAddTreatmentButton.setObjectName("petInfoAddTreatmentButton")
        #this is the "add allergy" button.
        self.petInfoAddAllergyButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoAddAllergyButton.setGeometry(QtCore.QRect(7, 125, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.petInfoAddAllergyButton.setFont(font)
        self.petInfoAddAllergyButton.setStyleSheet("background: orange;")
        self.petInfoAddAllergyButton.setObjectName("petInfoAddAllergyButton")
        #this is the TABLE widget on the right first side of the screen for "vaccination" table of the db
        self.petInfoVaccinationTable = QtWidgets.QTableWidget(self.petInfoWidget)
        self.petInfoVaccinationTable.setGeometry(QtCore.QRect(370, 40, 481, 160))
        self.petInfoVaccinationTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petInfoVaccinationTable.setObjectName("petInfoVaccinationTable")
        #this is the TABLE widget on the right second side of the screen for "treatments" table of the db
        self.petInfoTreatmentTable = QtWidgets.QTableWidget(self.petInfoWidget)
        self.petInfoTreatmentTable.setGeometry(QtCore.QRect(370, 210, 481, 160))
        self.petInfoTreatmentTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petInfoTreatmentTable.setObjectName("petInfoTreatmentTable")
        #this is the TABLE widget on the right third side of the screen for "allergies" table of the db
        self.petInfoAllergiesTable = QtWidgets.QTableWidget(self.petInfoWidget)
        self.petInfoAllergiesTable.setGeometry(QtCore.QRect(370, 380, 481, 160))
        self.petInfoAllergiesTable.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petInfoAllergiesTable.setObjectName("petInfoAllergiesTable")
        
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
        self.addPetAddVaccinationButton.setText(_translate("VetWindow", "Add Vaccination"))
        self.addPetAddTreatmentButton.setText(_translate("VetWindow", "Add Treatment"))
        self.addPetAddAllergyButton.setText(_translate("VetWindow", "Add Allergy"))

        self.addPetNameLabel.setText(_translate("VetWindow", "Pet Name:"))
        self.addPetdateOfBirthLabel.setText(_translate("VetWindow", "Date of Birth:"))


        self.petInfoBackButton.setText(_translate("VetWindow", "Back"))
        self.petInfoAddVaccinationButton.setText(_translate("VetWindow", "Add Vaccination"))
        self.petInfoAddTreatmentButton.setText(_translate("VetWindow", "Add Treatment"))
        self.petInfoAddAllergyButton.setText(_translate("VetWindow", "Add Allergy"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(self.searchTab), _translate("VetWindow", "Search"))
        self.label.setText(_translate("VetWindow", "My Appointments"))
        self.createAppointmentTable.setText(_translate("VetWindow", "Create Appointment"))
        self.vetTabs.setTabText(self.vetTabs.indexOf(self.myAppointmentsTab), _translate("VetWindow", "My Appointments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VetWindow = QtWidgets.QMainWindow()
    ui_login = Ui_VetWindow()
    ui_login.setupUi(VetWindow)

    VetWindow.show()
    sys.exit(app.exec_())

