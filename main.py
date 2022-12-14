import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Pages.LoginPage import *
from Pages.PetOwnerPage import *
from Pages.vetPage import *
from db.db_initialize import *
import auth_operation
import hashlib
import pet_owner_operations as poo
import vet_operations as vet
import json

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
        pass
    else:
        searched_pet_id = ui_vet.searchPetField.text() # gettin ID of the searched pet.
        ui_vet.searchPetField.clear()
        print(searched_pet_id)
        #ui_vet.searchTab.setVisible(False)
        ui_vet.searchPetField.clearFocus()
        ui_vet.petInfoWidget.setVisible(True)
        ui_vet.petInfoBackButton.clicked.connect(showSearchPage)

        # DB operations for regarding pet :
        
    
def showSearchPage():
    ui_vet.petInfoWidget.setVisible(False)
    ui_vet.searchTab.setVisible(True)

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
    ui_login.showPass.stateChanged.connect(showPassword)
    sys.exit(app.exec_())
