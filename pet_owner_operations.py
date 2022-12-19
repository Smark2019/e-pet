import sqlite3
from classes.Pet import Pet
from classes.Vaccination import Vaccination
from classes.Appointment import Appointment
from classes.Allergy import Allergy
from classes.Treatment import Treatment

def get_vet(vet_Id):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
   
    query = """SELECT * FROM user WHERE id = ?"""
    cursor.execute(query, (vet_Id,))
    vet = cursor.fetchone()

    return vet

def get_pet(pet_Id):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
   
    query = """SELECT * FROM pet WHERE id = ?"""
    cursor.execute(query, (pet_Id,))
    pet = cursor.fetchone()

    return pet


def get_list_of_pets(owner_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    pet_list = []
    pet_list_query = """SELECT * FROM pet WHERE owner_ID = ?"""
    cursor.execute(pet_list_query, (owner_ID,))
    pet_list = cursor.fetchall()
    
    """
    id = pet_list[0][0]
    name = pet_list[0][1]
    date_of_birth = pet_list[0][2]
    species = pet_list[0][3]
    gender = pet_list[0][4]
    sterility = pet_list[0][5]
    health_status = pet_list[0][6]
    owner_ID = pet_list[0][7]
    
    Pet(name, date_of_birth, species, gender, sterility, health_status, owner_ID, id)
    
    """

    # turn each pet list object into a pet object with fields
    for i in range(len(pet_list)):
        newPet = Pet(pet_list[i][1], pet_list[i][2], pet_list[i][3],
                     pet_list[i][4], pet_list[i][5], pet_list[i][6], pet_list[i][7],pet_list[i][0])
        pet_list[i] = newPet

    connection.close()
    return pet_list


def get_appointments(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT * FROM appointment WHERE pet_ID = ?"""
    cursor.execute(appointment_search_query, (pet_ID,))
    appointments = cursor.fetchall()
    # turn each pet list object into a pet object with fields
    for i in range(len(appointments)):
        newAppointment = Appointment(appointments[i][1], appointments[i][2], appointments[i][3],
                                     appointments[i][4], appointments[i][5], appointments[i][0])
        appointments[i] = newAppointment
    connection.close()
    return appointments


def get_treatments(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    treatment_list = []
    treatment_list_query = """SELECT * FROM treatment WHERE pet_ID = ?"""
    cursor.execute(treatment_list_query, (pet_ID,))
    treatment_list = cursor.fetchall()

    for i in range(len(treatment_list)):
        newTreatment = Treatment(treatment_list[i][1], treatment_list[i][2], treatment_list[i][3],
                                 treatment_list[i][4], treatment_list[i][5], treatment_list[i][0])
        treatment_list[i] = newTreatment
    connection.close()
    return treatment_list


def get_allergies(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    allergy_list = []
    allergy_list_query = """SELECT * FROM allergy WHERE pet_ID = ?"""
    cursor.execute(allergy_list_query, (pet_ID,))
    allergy_list = cursor.fetchall()
    for i in range(len(allergy_list)):
        newAllergy = Allergy(
             allergy_list[i][1], allergy_list[i][2], allergy_list[i][3], allergy_list[i][4], allergy_list[i][0])
        allergy_list[i] = newAllergy
    connection.close()
    return allergy_list


def get_vaccination_card(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    vaccination_list = []
    vaccination_list_query = """SELECT * FROM vaccination WHERE pet_ID = ?"""
    cursor.execute(vaccination_list_query, (pet_ID,))
    vaccination_list = cursor.fetchall()

    # turn each vaccination list object into a vaccination object with fields
    for i in range(len(vaccination_list)):
        vaccination_list[i] = Vaccination(vaccination_list[i][1], vaccination_list[i]
                                          [2], vaccination_list[i][3], vaccination_list[i][4], vaccination_list[i][5],vaccination_list[i][6], vaccination_list[i][0])

    connection.close()
    return vaccination_list


# yapamadık xd

# gets appointments where one week is left


def fetch_appointments_in_next_week(owner_ID):

    appointment_list = []
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT app.id,app.pet_ID, app.vet_ID, app.date_of_appointment, 
    app.description, app.vaccinations FROM appointment as app LEFT join pet as p on app.pet_ID = p.id   
    WHERE  owner_ID = ? AND date(substr(date_of_appointment, 7, 4) || '-' || substr(date_of_appointment, 4, 2) 
    || '-' || substr(date_of_appointment, 1, 2)) BETWEEN date('now') AND date('now', '+7 days')"""
    cursor.execute(appointment_search_query, (owner_ID,))
    appointments = cursor.fetchall()

    for i in range(len(appointments)):
        newAppointment = Appointment(appointments[i][1], appointments[i][2], appointments[i][3],
                                     appointments[i][4], appointments[i][5], appointments[i][0])
        appointment_list.append(newAppointment)
        
    connection.close()
    return appointment_list

# gets appointments where one day is left


def fetch_appointments_for_tomorrow(owner_ID):
    appointment_list = []
    
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT app.id,app.pet_ID, app.vet_ID, app.date_of_appointment, 
    app.description, app.vaccinations FROM appointment as app LEFT join pet as p on app.pet_ID = p.id 
    WHERE date(substr(date_of_appointment, 7, 4) || '-' || substr(date_of_appointment, 4, 2) || '-' ||
    substr(date_of_appointment, 1, 2)) = date('now', '+1 days') AND owner_ID = ?"""
    cursor.execute(appointment_search_query, (owner_ID,))
    appointments = cursor.fetchall()
    
    for i in range(len(appointments)):
        newAppointment = Appointment(appointments[i][1], appointments[i][2], appointments[i][3],
                                     appointments[i][4], appointments[i][5], appointments[i][0])
        appointment_list.append(newAppointment)
    
    connection.close()
    return appointment_list
