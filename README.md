# e-PET Software

> *A software for pet owners and veterinarians to keep track of the pets!*

This repository holds the source code of the e-Pet software that is created as a project for the CS 320 (Software Engineering) course in Ozyegin University, Istanbul, Turkey.

<br />
<p align="center">
    <img src="media/logo.png" alt="e-Pet Software Logo" width="600" height="350">
  </a>
</p>

<p> </p>

[![Python Pytest](https://github.com/durmusberk/cs320_project/actions/workflows/python-app.yml/badge.svg)](https://github.com/durmusberk/cs320_project/actions/workflows/python-app.yml)

### Technical Details

The software is completely developed using Python 3. For the graphical user interface (GUI), PyQt5 library is used. The main design of the appearance is made with Qt Designer. After that, the *.ui* files are converted into *.py* files and rearranged for implementing the details.

The database named *epet_database.db* keeps the entire software data in 6 different tables which are;

* *user:* Keeps both the pet owners, and the veterinarian information.
* *pet:* Keeps the pet information.
* *appointment:* Keeps the appointment information of the veterinarian for the specific pets.
* *treatment:* Keeps the treatment records of the pets.
* *vaccination:* Keeps the vaccination records of the pets.
* *allergy:* Keeps the allergy records of the pets.

The rows of the database is created by combining random data in *db_initialize.py* file.

### Requirements

* Install all the libraries in the *requirements.txt* file.

### Instructions

To run the software, open terminal, go to the main directory of the project, and run:

```sh
$ python main.py
```

To log in to the system, user need to enter an ID, and a password. The user can be either a pet owner, or a veterinarian. The information of the users are kept in the database as an encrypted format. For testing purposes, these id-password pairs can be used to log in:

* **Pet owner:**
  * *User ID:* 10824441638
  * *Password:* tyortiz123
* **Veterinarian:**
  * *User ID:* 11727904499
  * *Password:* ikeeastman123

## Application ScreenShots
![Alt text](media/Login%20Page.png "Epet Software Login Page")
![Alt text](media/Pet%20Owner%20-%20My%20Appointments%20List.png"Pet Owner - My Appointments List")
![Alt text](media/PetOwner%20-%20My%20Pet%20List.png"Pet Owner - My Pets List")
![Alt text](media/Vet%20-%20%20Search%20Pet.png"Vet - Search Pet")
![Alt text](media/Vet%20-%20Add%20Pet.png"Vet - Add Pet")
![Alt text](media/Vet%20-%20Add%20Vaccination.png "Vet - Add Vaccination")
![Alt text](media/Vet%20-%20Create%20Appointment.png "Vet - Create Appointment")
![Alt text](media/Vet%20-%20Show%20Info%20%26%20Add%20Vacc%2C%20Appointment%20and%20Treatment.png"Vet - Show Info & Add Vacc, Appointment and Treatment")







## Contact

[![Salih Metin Arkanöz](https://img.shields.io/badge/salih_metin_arkanöz-metin.arkanoz@ozu.edu.tr-yellow?style=for-the-badge&logo=mail)](mailto:metin.arkanoz@ozu.edu.tr)

[![Atahan Çaldır](https://img.shields.io/badge/atahan_çaldır-atahan.caldir@ozu.edu.tr-red?style=for-the-badge&logo=mail)](mailto:atahan.caldir@ozu.edu.tr)

[![Durmuş Berk](https://img.shields.io/badge/durmuş_berk-durmus.berk@ozu.edu.tr-blue?style=for-the-badge&logo=mail)](mailto:durmus.berk@ozu.edu.tr)

[![Selim Çavaş](https://img.shields.io/badge/selim_çavaş-selim.cavas@ozu.edu.tr-green?style=for-the-badge&logo=mail)](mailto:selim.cavas@ozu.edu.tr)

[![Cansu Çelik](https://img.shields.io/badge/cansu_çelik-cansu.celik@ozu.edu.tr-yellowgreen?style=for-the-badge&logo=mail)](mailto:cansu.celik@ozu.edu.trk)
