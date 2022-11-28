from PyQt5 import uic

#this python file generates the python file from the ui file
with open("Pages/LoginPage.py", "w", encoding="utf-8") as f:
    uic.compileUi("UI Files/login.ui", f)
