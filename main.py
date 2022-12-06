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

# Main Window            

def authenticate():
    """_summary_ : Authenticates the user and logs them in if the credentials are correct.
    """
    
    id = ui.idField.text()
    password = hashlib.sha256(ui.passField.text().encode('utf-8')).hexdigest()

    
    result = auth_operation.authentification(id, password)
    if result == 1:
        ui.statusbar.showMessage("Login Successful", 5000)
        print("Login Successful")
        #getInput(id)
    elif result == 2:
        ui.statusbar.showMessage("User unblocked! Login Successful!", 5000)
        print("User unblocked! Login Successful!")
    elif result == 0:
        ui.statusbar.showMessage("Wrong Password", 5000)
        print("Wrong password.")
    elif result == -1:
        ui.statusbar.showMessage("User not found", 5000)
        print("User not found.")
    elif result == -2:
        ui.statusbar.showMessage("5th Failed Attempt. User Blocked!", 5000)
        print("5th Failed Attempt. User Blocked!")
    elif result == -3:
        ui.statusbar.showMessage("User Blocked! Try Again in 5 min!", 5000)
        print("User Blocked! Try Again in 5 min!")
    elif result == -4:
        ui.statusbar.showMessage("User unblocked! Wrong Password!", 5000)
        print("User unblocked! Wrong Password!")
    else:
        ui.statusbar.showMessage("Unknown Error", 5000)
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
    if ui.showPass.isChecked():
        ui.passField.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        ui.passField.setEchoMode(QtWidgets.QLineEdit.Password)


def getInput(id):
    pet_ID_list = []
    a = poo.get_list_of_pets(id)
    for item in a:
        pet_ID_list.append(item.id)
        print(item.to_string())
    print(pet_ID_list)
    for i in pet_ID_list:

        for item in poo.get_vaccination_card(i):
            print(item.to_string())

        for item in poo.get_allergies(i):
            print(item.to_string())

        for item in poo.get_treatments(i):
            print(item.to_string())

        for item in poo.get_appointments(i):
            print(item.to_string())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_LoginWindow()
    
    ui.setupUi(window)
    window.show()

    initialize_db()  # initialize the database if it doesn't exist
    
    
    ui.loginButton.clicked.connect(authenticate)
    ui.showPass.stateChanged.connect(showPassword)
    sys.exit(app.exec_())
