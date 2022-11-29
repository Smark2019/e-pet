import sqlite3


def get_list_of_pets(owner_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    pet_list = []
    pet_list_query = """SELECT * FROM pet WHERE owner_ID = ?"""
    cursor.execute(pet_list_query, (owner_ID,))
    pet_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return pet_list


def get_pet_info(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    pet_info = []
    pet_info_query = """SELECT * FROM pet WHERE id = ?"""
    cursor.execute(pet_info_query, (pet_ID,))
    pet_info = cursor.fetchall()
    connection.commit()
    connection.close()
    return pet_info


def get_vaccination_card(pet_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    vaccination_list = []
    vaccination_list_query = """SELECT * FROM vaccination WHERE pet_ID = ?"""
    cursor.execute(vaccination_list_query, (pet_ID,))
    vaccination_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return vaccination_list


# fix this method according to needs


def add_appointment(appointment):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_add_query = """INSERT INTO appointment VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(appointment_add_query, (appointment.pet_ID, appointment.vet_ID, appointment.date_of_appointment,
                                           appointment.description, appointment.vaccinations))
    connection.commit()
    connection.close()

# gets appointments where one week is left


def get_appointment_in_next_week(owner_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT * FROM appointment WHERE date_of_appointment = date('now', '+7 days' AND owner_ID = ?)"""
    cursor.execute(appointment_search_query, (owner_ID,))
    appointments = cursor.fetchall()
    connection.commit()
    connection.close()
    return appointments

# gets appointments where one day is left


def get_appointment_for_tomorrow(owner_ID):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    appointment_search_query = """SELECT * FROM appointment WHERE date_of_appointment = date('now', '+1 days' AND owner_ID = ?)"""
    cursor.execute(appointment_search_query, (owner_ID,))
    appointments = cursor.fetchall()
    connection.commit()
    connection.close()
    return appointments
