import sqlite3


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
    return pet


def add_pet(pet):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    pet_add_query = """INSERT INTO pet VALUES(?, ?, ?, ?, ?, ?, ?)"""
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

    vaccination_add_query = """INSERT INTO vaccination VALUES(?, ?, ?, ?, ?, ?)"""
    cursor.execute(vaccination_add_query, (vaccination.pet_ID, vaccination.vet_ID, vaccination.name,
                                           vaccination.date_of_vaccination, vaccination.dose_given, vaccination.count))
    connection.commit()
    connection.close()


def add_appointment(appointment):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_add_query = """INSERT INTO appointment VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(appointment_add_query, (appointment.pet_ID, appointment.vet_ID, appointment.date_of_appointment,
                                           appointment.description, appointment.vaccinations))
    connection.commit()
    connection.close()


def add_treatment(treatment):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    treatment_add_query = """INSERT INTO treatment VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(treatment_add_query, (treatment.pet_ID,
                   treatment.vet_ID, treatment.description, treatment.used_medicine, treatment.date_of_treatment))
    connection.commit()
    connection.close()


def add_allergy(allergy):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    allergy_add_query = """INSERT INTO allergy VALUES(?, ?, ?, ?)"""
    cursor.execute(allergy_add_query, (allergy.pet_ID,
                   allergy.vet_ID, allergy.description, allergy.drugs))
    connection.commit()
    connection.close()


def get_appointments_in_next_3days():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT * FROM appointment WHERE date_of_appointment BETWEEN date('now') AND date('now', '+3 days') ORDER BY date_of_appointment ASC"""
    cursor.execute(appointment_search_query)
    appointments = cursor.fetchall()
    connection.close()
    return appointments
