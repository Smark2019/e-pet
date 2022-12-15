import sys
from classes import Appointment,Vaccination,Allergy,Treatment
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# PAGES
from Pages.LoginPage import *
from Pages.PetOwnerPage import *
from Pages.vetPage import *
#-----------#-----------#-----------
from db.db_initialize import *
import auth_operation
import hashlib
import pet_owner_operations as poo
import vet_operations as vo
import json
import time
from datetime import datetime, timedelta
# Main Window 


def getCredentialsFromJSON():
    # Opening JSON file
    # JSON format: {"credentials": [{"id": id, "password": "password"}]}
    
    credentials = []
    try:
        f = open('credentials.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        for i in data['credentials']:
            credentials.append(i)
        
        # Closing file
        f.close()    
    except:
        print("Error loading credentials.json")
        
    return credentials 

def authenticate():
    """_summary_ : Authenticates the user and logs them in if the credentials are correct.
    """
    global id
    id = ui_login.idField.text()
    password = hashlib.sha256(ui_login.passField.text().encode('utf-8')).hexdigest()

    credentials = getCredentialsFromJSON()
    
    if len(credentials) == 0:
        print("No sample credentials found.")
    else:
        print("Sample credentials found. Entering sample credentials.")
        
        id = credentials[0]['id']
        password = hashlib.sha256(credentials[0]['password'].encode('utf-8')).hexdigest()
    global is_vet
    result, is_vet = auth_operation.authentification(id, password)


    if result == 1 and is_vet:
        ui_login.statusbar.showMessage("Login Successful for Vet", 5000)
        print("Login Successful for Vet")
        window.close()
        ui_vet.setupUi(window)
        window.show()
        navigator(id)
    
    elif result == 1 and not is_vet:
        ui_login.statusbar.showMessage("Login Successful for Pet Owner", 5000)
        print("Login Successful for Pet Owner")
        window.close()
        ui_petOwner.setupUi(window)
        window.show()
        navigator(id)

    elif result == 2:
        ui_login.statusbar.showMessage("User unblocked! Login Successful!", 5000)
        print("User unblocked! Login Successful!")
    elif result == 0:
        ui_login.statusbar.showMessage("Wrong Password", 5000)
        print("Wrong password.")
    elif result == -1:
        ui_login.statusbar.showMessage("User not found", 5000)
        print("User not found.")
    elif result == -2:
        ui_login.statusbar.showMessage("5th Failed Attempt. User Blocked!", 5000)
        print("5th Failed Attempt. User Blocked!")
    elif result == -3:
        ui_login.statusbar.showMessage("User Blocked! Try Again in 5 min!", 5000)
        print("User Blocked! Try Again in 5 min!")
    elif result == -4:
        ui_login.statusbar.showMessage("User unblocked! Wrong Password!", 5000)
        print("User unblocked! Wrong Password!")
    else:
        ui_login.statusbar.showMessage("Unknown Error", 5000)
        print("Unknown Error")
    """ msg = QMessageBox() #create a message box to show the error
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Wrong ID or Password!")
    msg.setInformativeText('Please try again.')
    msg.setWindowTitle("Error!")
    msg.exec_() """


def showPassword():
    """_summary_ : Shows the password in plain text when the user clicks the show password button. 
    Otherwise, it hides the password.
    """
    if ui_login.showPass.isChecked():
        ui_login.passField.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        ui_login.passField.setEchoMode(QtWidgets.QLineEdit.Password)


def navigator(id):
    counter = 0
    pet_ID_list = []
    if(is_vet): # this block runs if user is Vet.
        
        ui_vet.searchPetButton.clicked.connect(showPetInfoPage)
        ui_vet.searchPetField.returnPressed.connect(showPetInfoPage)
        getDataToMyAppointmentsTab(id)
        

    else: # this block runs if user is Pet Owner.
        pet_list = poo.get_list_of_pets(id)
        for pet in pet_list:
            pet_ID_list.append(pet.id)
            print(pet.to_string())
            ui_petOwner.myPetsList.addItem(pet.name) # shows names of pet of regarding pet owner
            print(pet_ID_list)

        for id in pet_ID_list:

            for vacc_card in poo.get_vaccination_card(id):
                print(vacc_card.to_string())

            for allergy in poo.get_allergies(id):
                print(allergy.to_string())

            for treatmen in poo.get_treatments(id):
                print(treatmen.to_string())
            
            for appointment in poo.get_appointments(id):
                pet = poo.get_pet(appointment.pet_ID)
                ui_petOwner.myAppointmentsTable.setItem(counter , 0, QTableWidgetItem(str(pet[1])))

                print(appointment.to_string())
                vet = poo.get_vet(appointment.vet_ID)
                ui_petOwner.myAppointmentsTable.setItem(counter , 1, QTableWidgetItem(str(vet[3])+" "+str(vet[4])))
                ui_petOwner.myAppointmentsTable.setItem(counter , 2, QTableWidgetItem(str(appointment.date_of_appointment)))

                counter+=1
        


    

def showPetInfoPage():
    if(ui_vet.searchPetField.text() == ""):
        msg = QMessageBox() #create a message box to show the error
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Please enter a Pet ID")
        msg.setInformativeText('Please try again.')
        msg.setWindowTitle("Error!")
        msg.exec_()
    else:
        global searched_pet_id
        searched_pet_id = ui_vet.searchPetField.text() # getting ID of the searched pet.
        ui_vet.searchPetField.clear()
        print(searched_pet_id)
        
        try:
            # following first part runs for controlling of "Save" buttons at PopUps:
            
            
            try:


                ui_vet.petInfoAddVaccinationButton.clicked.connect(conductAddVaccinationPopUp)
            except Exception as e: print(e)
            
            #ui_vet.popUi.saveAllergyButton.clicked.connect(conductAddAllergyPopUp)
            #ui_vet.popUi.saveTreatmentButton.clicked.connect(conductAddTreatmentPopUp)
            
            # DB operations for regarding pet : ( petInfoList )   
            pet_displayed = vo.search_pet(searched_pet_id)
            colored_item = QListWidgetItem("ID")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.id}")
            colored_item = QListWidgetItem("Name")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.name}")
            colored_item = QListWidgetItem("Date of Birth")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.date_of_birth}")
            colored_item = QListWidgetItem("Species")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.species}")
            colored_item = QListWidgetItem("Gender")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.gender}")
            colored_item = QListWidgetItem("Sterility")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{bool(pet_displayed.sterility)}")
            colored_item = QListWidgetItem("Owner ID")
            colored_item.setBackground(QColor("#7fc97f"))
            ui_vet.petInfoList.addItem(colored_item)
            ui_vet.petInfoList.addItem(f"{pet_displayed.owner_ID}")
            ui_vet.searchPetField.clearFocus()
            ui_vet.petInfoWidget.setVisible(True)
            ui_vet.petInfoBackButton.clicked.connect(showSearchPage)

            # DB operations for regarding pet : ( pet Vaccination List )  
            vacc_list = poo.get_vaccination_card(searched_pet_id)
            
            if(len(vacc_list) != 0):
                for vacc in vacc_list:

                    ui_vet.petInfoVaccinationTable.setItem(vacc_list.index(vacc) , 0, QTableWidgetItem(str(vacc.vet_ID)))
                    ui_vet.petInfoVaccinationTable.setItem(vacc_list.index(vacc) , 1, QTableWidgetItem(str(vacc.name)))
                    ui_vet.petInfoVaccinationTable.setItem(vacc_list.index(vacc) , 2, QTableWidgetItem(str(vacc.date_of_vaccination)))
                    ui_vet.petInfoVaccinationTable.setItem(vacc_list.index(vacc) , 3, QTableWidgetItem(str(vacc.dose_given)))
                    ui_vet.petInfoVaccinationTable.setItem(vacc_list.index(vacc) , 4, QTableWidgetItem(str(vacc.count)))

            # DB operations for regarding pet : ( pet Treatment List )  
            treatment_list = poo.get_treatments(searched_pet_id)
            
            if(len(treatment_list) != 0):
                for treatment in treatment_list:
    
                    ui_vet.petInfoTreatmentTable.setItem(treatment_list.index(treatment) , 0, QTableWidgetItem(str(treatment.vet_ID)))
                    ui_vet.petInfoTreatmentTable.setItem(treatment_list.index(treatment) , 1, QTableWidgetItem(str(treatment.description)))
                    ui_vet.petInfoTreatmentTable.setItem(treatment_list.index(treatment) , 2, QTableWidgetItem(str(treatment.used_medicine)))
                    ui_vet.petInfoTreatmentTable.setItem(treatment_list.index(treatment) , 3, QTableWidgetItem(str(treatment.date_of_treatment)))
                    
            
            # DB operations for regarding pet : ( pet Allergies List )  
            allergy_list = poo.get_allergies(searched_pet_id)
            if(len(allergy_list) != 0):
                for allergy in allergy_list:
                    print(allergy.drugs)
                    ui_vet.petInfoAllergiesTable.setItem(allergy_list.index(allergy) , 0, QTableWidgetItem(str(allergy.vet_ID)))
                    ui_vet.petInfoAllergiesTable.setItem(allergy_list.index(allergy) , 1, QTableWidgetItem(str(allergy.description)))
                    ui_vet.petInfoAllergiesTable.setItem(allergy_list.index(allergy) , 2, QTableWidgetItem(str(allergy.drugs)))
            
                 
            

        except:
            msg = QMessageBox() #create a message box to show the error
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Pet does not exist!")
            msg.setInformativeText('Please try again.')
            msg.setWindowTitle("Error!")
            msg.exec_()


        
    
def showSearchPage():
    ui_vet.petInfoWidget.setVisible(False)
    ui_vet.searchTab.setVisible(True)
    ui_vet.petInfoList.clear()

def getDataToMyAppointmentsTab(vet_id): # tested and it works properly.
        
    # DB operations for regarding pet : ( pet Allergies List )  
        appointments_list = vo.get_appointments_in_next_3days(vet_id)
        print(appointments_list)
        if(len(appointments_list) != 0):
            for appointment in appointments_list:

                ui_vet.myAppointmentsTable.setItem(appointments_list.index(appointment) , 0, QTableWidgetItem(str(appointment.pet_ID)))
                ui_vet.myAppointmentsTable.setItem(appointments_list.index(appointment) , 1, QTableWidgetItem(str(appointment.vet_ID)))
                ui_vet.myAppointmentsTable.setItem(appointments_list.index(appointment) , 2, QTableWidgetItem(str(appointment.date_of_appointment)))
                ui_vet.myAppointmentsTable.setItem(appointments_list.index(appointment) , 3, QTableWidgetItem(str(appointment.description)))
                ui_vet.myAppointmentsTable.setItem(appointments_list.index(appointment) , 4, QTableWidgetItem(str(appointment.vaccinations)))
        
def conductAddVaccinationPopUp(): # ensures that VaccPopUp opened now
    print("AddVaccinationPopUp OPENS")
    ui_vet.popUi.saveVaccinationButton.clicked.connect(saveVacc)

def saveVacc():
        # db operations starts after checking obligatory fields:

        if(ui_vet.popUi.vaccinationNameField.text() != "" and ui_vet.popUi.vaccinationCountField.text() != "" and ui_vet.popUi.vaccinationDoseGivenField.text() != "" and ui_vet.popUi.dateOfVaccinationField.text() != ""):

            vaccName = ui_vet.popUi.vaccinationNameField.text()
            vaccCount = ui_vet.popUi.vaccinationCountField.text()
            vaccDose = ui_vet.popUi.vaccinationDoseGivenField.text()
            vaccDate = ui_vet.popUi.dateOfVaccinationField.text()
            vaccDate = datetime.strptime(vaccDate, "%d.%m.%Y %H:%M")
            vaccDate = datetime.strftime(vaccDate, "%d-%m-%Y %H:%M")


            savedVacc = Vaccination.Vaccination(searched_pet_id,id,vaccName,vaccDate,vaccDose,vaccCount)
            vo.add_vaccination(savedVacc)
            msg = QMessageBox() #create a message box to show the error
            msg.setIcon(QMessageBox.Information)
            msg.setText("Your Vacc Saved !")
            msg.setInformativeText('')
            msg.setWindowTitle("Succesfully Saved!")
            msg.exec_()
            ui_vet.window.close()
        else:
            msg = QMessageBox() #create a message box to show the error
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Cannot leave fields as empty!")
            msg.setInformativeText('Please try again.')
            msg.setWindowTitle("Error!")
            msg.exec_()

            


def conductAddAllergyPopUp():
    print("AddAllergyPopUp OPENS")
def conductAddTreatmentPopUp():
    print("AddTreatmentPopUp OPENS")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui_login = Ui_LoginWindow() # login page generated
    ui_login.setupUi(window) # login page placed into window

    ui_vet = Ui_VetWindow() # vet page generated

    ui_petOwner = Ui_PetOwnerWindow() #petOwner page generated




    window.show()

    initialize_db()  # initialize the database if it doesn't exist
    
    
    ui_login.loginButton.clicked.connect(authenticate)
    ui_login.idField.returnPressed.connect(authenticate)
    ui_login.passField.returnPressed.connect(authenticate)
    ui_login.showPass.stateChanged.connect(showPassword)

    sys.exit(app.exec_())
