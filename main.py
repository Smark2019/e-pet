import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Pages.LoginPage import *
import db_initialize
import auth_operation
import hashlib

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_LoginWindow()
ui.setupUi(window)
window.show()

db_initialize.initialize_db() #initialize the database if it doesn't exist

def authenticate():
    """_summary_ : Authenticates the user and logs them in if the credentials are correct.
    """
    id = ui.idField.text()
    password = hashlib.sha256(ui.passField.text().encode('utf-8')).hexdigest()

    result = auth_operation.authentification(id,password)
    if result == 1: 
        ui.statusbar.showMessage("Login Successful", 5000)
        print("Login Successful")
    elif result == 0:
        ui.statusbar.showMessage("Wrong Password", 5000)
        print("Wrong password.")
    else:
        ui.statusbar.showMessage("Wrong ID or Password!",5000)
        print("Wrong ID or password.")

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
        

ui.loginButton.clicked.connect(authenticate)
ui.showPass.stateChanged.connect(showPassword)

sys.exit(app.exec_())