import sqlite3
from classes.Appointment import Appointment
from classes.Pet import Pet


def search_pet(petID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    pet_search_query = """SELECT * FROM pet WHERE id = ?"""
    cursor.execute(pet_search_query, (petID,))
    pet = cursor.fetchone()

    # if pet does not exist return -1
    if pet == None:
        return -1

    connection.close()
    return Pet(pet[1], pet[2], pet[3], pet[4], pet[5], pet[6], pet[7], pet[0])


def add_pet(pet):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    pet_add_query = """INSERT INTO pet(name,date_of_birth,species,gender,sterility,health_status,owner_ID) VALUES(?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(pet_add_query, (pet.name, pet.date_of_birth,
                   pet.species, pet.gender, pet.sterility, pet.health_status, pet.owner_ID))

    connection.commit()
    connection.close()


def edit_pet(pet_id, sterility, health_status, owner_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    pet_edit_query = """UPDATE pet SET sterility = ?, health_status = ?, owner_ID = ? WHERE id = ?"""
    cursor.execute(pet_edit_query, (sterility,
                   health_status, owner_ID, pet_id))
    connection.commit()
    connection.close()


def add_vaccination(vaccination):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    vaccination_add_query = """INSERT INTO vaccination(pet_ID,vet_ID,name,date_of_vaccination,dose_given,count) VALUES(?, ?, ?, ?, ?, ?)"""
    cursor.execute(vaccination_add_query, (vaccination.pet_ID, vaccination.vet_ID, vaccination.name,
                                           vaccination.date_of_vaccination, vaccination.dose_given, vaccination.count))
    connection.commit()
    connection.close()


def add_appointment(appointment):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_add_query = """INSERT INTO appointment(pet_ID,vet_ID,date_of_appointment,description,vaccinations) VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(appointment_add_query, (appointment.pet_ID, appointment.vet_ID, appointment.date_of_appointment,
                                           appointment.description, appointment.vaccinations))
    connection.commit()
    connection.close()


def add_treatment(treatment):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    treatment_add_query = """INSERT INTO treatment(pet_ID,vet_ID,description,used_medicine,date_of_treatment) VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(treatment_add_query, (treatment.pet_ID,
                   treatment.vet_ID, treatment.description, treatment.used_medicine, treatment.date_of_treatment))
    connection.commit()
    connection.close()


def add_allergy(allergy):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    allergy_add_query = """INSERT INTO allergy(pet_ID,vet_ID,description,drugs) VALUES(?, ?, ?, ?)"""
    cursor.execute(allergy_add_query, (allergy.pet_ID,
                   allergy.vet_ID, allergy.description, allergy.drugs))
    connection.commit()
    connection.close()


def get_appointments_in_next_3days(vet_ID):
    appointment_list = []
    
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT * FROM appointment WHERE vet_ID = ? AND date(substr(date_of_appointment, 7, 4) || '-' || substr(date_of_appointment, 4, 2) || '-' || substr(date_of_appointment, 1, 2)) BETWEEN date('now') AND date('now', '+3 days') ORDER BY date_of_appointment ASC"""
    
    cursor.execute(appointment_search_query, (vet_ID,))
    appointments = cursor.fetchall()
    connection.close()
    for item in appointments:
        appointment_list.append(Appointment(item[1], item[2], item[3], item[4], item[5],item[0]))
    return appointment_list
