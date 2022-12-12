import vet_operations
from classes import Pet, Vaccination, Appointment, Treatment, Allergy
import sqlite3
import pet_owner_operations
import time
from datetime import datetime, timedelta
# Pytest is used to run the test run with python -m pytest


def test_get_list_of_pets():
    ts = time.time()
    test_pet = Pet.Pet("Olive", "12.12.2021", "Dog",
                       "Male", "No", "Healthy", ts, 1)

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    pet_add_query = """INSERT INTO pet(name,date_of_birth,species,gender,sterility,health_status,owner_ID) VALUES(?, ?, ?, ?, ?, ?, ?)"""
    delete_query = """DELETE FROM pet WHERE owner_ID = ?"""
    cursor.execute(pet_add_query, (test_pet.name, test_pet.date_of_birth,
                   test_pet.species, test_pet.gender, test_pet.sterility, test_pet.health_status, test_pet.owner_ID))

    connection.commit()
    test_pet_list = pet_owner_operations.get_list_of_pets(test_pet.owner_ID)
    is_found = False
    for pet in test_pet_list:
        if (pet.owner_ID == test_pet.owner_ID):
            is_found = True
            break

    cursor.execute(delete_query, (test_pet.owner_ID,))
    connection.commit()
    connection.close()
    assert is_found


def test_get_appointments():
    ts = time.time()
    test_app = Appointment.Appointment(ts, 11, "12.12.2022", "description",
                                       "test_vac", 13)

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    app_add_query = """INSERT INTO appointment(pet_ID,vet_ID,date_of_appointment,description,vaccinations) VALUES(?, ?, ?, ?, ?)"""
    delete_query = """DELETE FROM appointment WHERE pet_ID = ?"""
    cursor.execute(app_add_query, (test_app.pet_ID, test_app.vet_ID, test_app.date_of_appointment,
                                   test_app.description, test_app.vaccinations))
    connection.commit()

    # calling get_appointments func:
    test_apps = pet_owner_operations.get_appointments(test_app.pet_ID)

    is_found = False
    for appointment in test_apps:
        if (appointment.pet_ID == test_app.pet_ID):
            is_found = True
            break

    cursor.execute(delete_query, (test_app.pet_ID,))
    connection.commit()
    connection.close()
    assert is_found


def test_get_treatments():
    ts = time.time()
    test_treat = Treatment.Treatment(
        ts, "11", "This treatment is generated for test purpose.", "Apoquel Tablets for Dogs", "12.12.2022", 111)
    # db operations:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    test_treatment_add_query = """INSERT INTO treatment(pet_ID,vet_ID,description,used_medicine,date_of_treatment) VALUES(?, ?, ?, ?, ?)"""
    delete_query = """DELETE FROM treatment WHERE pet_ID = ?"""
    cursor.execute(test_treatment_add_query, (test_treat.pet_ID,
                   test_treat.vet_ID, test_treat.description, test_treat.used_medicine, test_treat.date_of_treatment))
    connection.commit()
    test_treatment_list = pet_owner_operations.get_treatments(
        test_treat.pet_ID)

    is_found = False
    for treatment in test_treatment_list:
        if (treatment.pet_ID == test_treat.pet_ID):
            is_found = True
            break

    cursor.execute(delete_query, (test_treat.pet_ID,))
    connection.commit()
    connection.close()
    assert is_found


def test_get_allergies():
    ts = time.time()
    test_allergy = Allergy.Allergy(ts, "11", "This allergy is generated for test purpose. ",
                                   "No Medicine", 123)
    # db op.s:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    allergy_add_query = """INSERT INTO allergy(pet_ID,vet_ID,description,drugs) VALUES(?, ?, ?, ?)"""
    delete_query = """DELETE FROM allergy WHERE pet_ID = ?"""
    cursor.execute(allergy_add_query, (test_allergy.pet_ID,
                   test_allergy.vet_ID, test_allergy.description, test_allergy.drugs))
    connection.commit()

    test_allergy_list = pet_owner_operations.get_allergies(test_allergy.pet_ID)
    is_found = False
    for allergy in test_allergy_list:
        if (allergy.pet_ID == test_allergy.pet_ID):
            is_found = True
            break

    cursor.execute(delete_query, (test_allergy.pet_ID,))
    connection.commit()
    connection.close()
    assert is_found


def test_get_vaccination_card():
    ts = time.time()
    test_vac = Vaccination.Vaccination(ts, "345",
                                       "HPP-B", "7.12.2022", "1.5 Mg", "1", 112)
    # db op.s:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    vaccination_add_query = """INSERT INTO vaccination(pet_ID,vet_ID,name,date_of_vaccination,dose_given,count) VALUES(?, ?, ?, ?, ?, ?)"""
    delete_query = """DELETE FROM vaccination WHERE pet_ID = ?"""
    cursor.execute(vaccination_add_query, (test_vac.pet_ID, test_vac.vet_ID, test_vac.name,
                                           test_vac.date_of_vaccination, test_vac.dose_given, test_vac.count))
    connection.commit()

    test_vac_list = pet_owner_operations.get_vaccination_card(test_vac.pet_ID)

    is_found = False
    for vacc in test_vac_list:
        if (vacc.pet_ID == test_vac.pet_ID):
            is_found = True
            break

    cursor.execute(delete_query, (test_vac.pet_ID,))
    connection.commit()
    connection.close()
    assert is_found


def test_fetch_appointments_in_next_week():
    ts = time.time()
    date_now = datetime.now()
    date_of_app = date_now + timedelta(days=7)
    date_of_app = datetime.strftime(date_of_app, "%m/%d/%y")

    test_pet = Pet.Pet("Olive", "12.12.2021", "Dog",
                       "Male", "No", "Healthy", ts, 1)

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    pet_add_query = """INSERT INTO pet(name,date_of_birth,species,gender,sterility,health_status,owner_ID) VALUES(?, ?, ?, ?, ?, ?, ?)"""
    get_pet_id = """SELECT id FROM pet WHERE owner_ID = ?"""

    cursor.execute(pet_add_query, (test_pet.name, test_pet.date_of_birth,
                   test_pet.species, test_pet.gender, test_pet.sterility, test_pet.health_status, test_pet.owner_ID))

    connection.commit()

    cursor.execute(get_pet_id, (test_pet.owner_ID,))
    pet_id = cursor.fetchone()

    test_pet.id = pet_id[0]

    test_app = Appointment.Appointment(test_pet.id, 11, date_of_app, "This appointment is generated for test purpose.",
                                       "vac1")

    app_add_query = """INSERT INTO appointment(pet_ID,vet_ID,date_of_appointment,description,vaccinations) VALUES(?, ?, ?, ?, ?)"""
    delete_pet_query = """DELETE FROM pet WHERE owner_ID = ?"""
    delete_app_query = """DELETE FROM appointment WHERE pet_ID = ?"""

    cursor.execute(app_add_query, (test_app.pet_ID, test_app.vet_ID, test_app.date_of_appointment,
                                   test_app.description, test_app.vaccinations))
    connection.commit()

    test_apps_list = pet_owner_operations.fetch_appointments_in_next_week(
        test_pet.owner_ID)
    is_found = False
    for app in test_apps_list:
        app.to_string()
        if (app.pet_ID == test_app.pet_ID):
            is_found = True
            break

    cursor.execute(delete_pet_query, (test_pet.owner_ID,))
    cursor.execute(delete_app_query, (test_app.id,))
    connection.commit()
    connection.close()
    assert is_found


def test_fetch_appointments_for_tomorrow():
    date_now = datetime.now()
    date_of_app = date_now + timedelta(days=1)
    date_of_app = datetime.strftime(date_of_app, "%m/%d/%y")

    test_vac = Vaccination.Vaccination("12345", "345",
                                       "HPP-B", date_of_app, "1.5 Mg", "1", 11)
    test_app = Appointment.Appointment("12345", 11, date_of_app, " This appointment is generated for test purpose.",
                                       test_vac, 1)
    # db operations:

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    app_add_query = """INSERT INTO appointment(pet_ID,vet_ID,date_of_appointment,description,vaccinations) VALUES(?, ?, ?, ?, ?)"""
    cursor.execute(app_add_query, (test_app.pet_ID, test_app.vet_ID, test_app.date_of_appointment,
                                   test_app.description, test_app.vaccinations))
    connection.commit()
    connection.close()

    test_apps_list = pet_owner_operations.fetch_appointments_for_tomorrow(
        test_app.ownerId)
    is_found = False
    for app in test_apps_list:
        if (app.id == test_app.id):
            is_found = True
            break
    assert is_found
