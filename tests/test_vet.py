import vet_operations
from classes import Pet, Vaccination, Appointment, Treatment, Allergy
import datetime
import sqlite3
import time
from datetime import datetime, timedelta

# Pytest is used to run the test run with python -m pytest


def test_invalid_search_pet():
    assert vet_operations.search_pet(123123123123) == -1


def test_able_to_add_pet():
    ts = time.time()
    test_pet = Pet.Pet(str(ts), "12.12.2021", "Dog",
                       "Male", "No", "Healthy", "12345")
    vet_operations.add_pet(test_pet)
    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()

    get_added_pet = """SELECT * FROM pet WHERE name = ? """
    delete_query = """DELETE FROM pet WHERE name = ?"""
    cursor.execute(get_added_pet, (test_pet.name,))

    result = cursor.fetchone()
    connection.commit()

    cursor.execute(delete_query, (test_pet.name,))
    connection.commit()
    connection.close()

    assert test_pet.name == result[1]


def test_edit_pet():
    ts = time.time()
    test_pet = Pet.Pet("Olive", "12-12-2021 9:21",
                       "Dog", "Male", 0, "Healthy", str(ts))

    vet_operations.add_pet(test_pet)

    get_pet_id = """SELECT id FROM pet WHERE owner_ID = ? """
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    cursor.execute(get_pet_id, (test_pet.owner_ID,))
    pet_id = cursor.fetchone()

    vet_operations.edit_pet(pet_id[0], 1, "Not Healthy", test_pet.owner_ID)

    get_added_pet = """SELECT * FROM pet WHERE owner_ID = ? """
    cursor.execute(get_added_pet, (test_pet.owner_ID,))
    result = cursor.fetchone()

    delete_query = """DELETE FROM pet WHERE owner_ID = ? """
    cursor.execute(delete_query, (test_pet.owner_ID,))
    connection.commit()
    connection.close()

    assert result[5] == 1 and result[6] == "Not Healthy"


def test_add_vaccination():
    ts = time.time()

    test_vac = Vaccination.Vaccination(ts, "345",
                                       "HPP-B", "7.12.2022", "1.5 Mg", "1")
    vet_operations.add_vaccination(test_vac)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM vaccination WHERE pet_ID = ? """
    delete_query = """DELETE FROM vaccination WHERE pet_ID = ?"""
    cursor.execute(get_added_pet, (test_vac.pet_ID,))
    result = cursor.fetchone()

    cursor.execute(delete_query, (test_vac.pet_ID,))
    connection.commit()
    connection.close()
    assert result[1] == test_vac.pet_ID


def test_add_appointment():
    ts = time.time()
    test_app = Appointment.Appointment(ts, 11, "12.12.2022", " This appointment is generated for test purpose.",
                                       "test_vac")
    vet_operations.add_appointment(test_app)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM appointment WHERE pet_ID = ? """
    delete_query = """DELETE FROM appointment WHERE pet_ID = ?"""
    cursor.execute(get_added_pet, (test_app.pet_ID,))
    result = cursor.fetchone()

    cursor.execute(delete_query, (test_app.pet_ID,))
    connection.commit()
    connection.close()

    assert result[1] == test_app.pet_ID


def test_add_treatment():
    ts = time.time()
    test_treat = Treatment.Treatment(
        int(ts), 11, "This treatment is generated for test purpose.", "Apoquel Tablets for Dogs", "12-12-2022 09:21")
    vet_operations.add_treatment(test_treat)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    print(test_treat.pet_ID)
    get_added_pet = """SELECT * FROM treatment WHERE pet_ID = ? """
    cursor.execute(get_added_pet, (test_treat.pet_ID,))
    result = cursor.fetchone()

    delete_query = """DELETE FROM treatment WHERE pet_ID = ?"""
    cursor.execute(delete_query, (test_treat.pet_ID,))
    connection.commit()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    assert result[1] == test_treat.pet_ID


def test_add_allergy():
    ts = time.time()
    test_allergy = Allergy.Allergy(ts, "11", "This allergy is generated for test purpose. ",
                                   "No Medicine")
    vet_operations.add_allergy(test_allergy)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM allergy WHERE pet_ID = ? """
    delete_query = """DELETE FROM allergy WHERE pet_ID = ?"""
    cursor.execute(get_added_pet, (test_allergy.pet_ID,))
    result = cursor.fetchone()

    cursor.execute(delete_query, (test_allergy.pet_ID,))
    connection.commit()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    assert result[1] == test_allergy.pet_ID


def test_get_appointments_in_next_3days():
    ts = time.time()
    date_now = datetime.now()
    date_of_last_app = date_now + timedelta(days=3)

    date_now = datetime.strftime(date_now, "%d-%m-%Y %H:%M")
    date_of_last_app = datetime.strftime(date_of_last_app, "%d-%m-%Y %H:%M")

    test_app1 = Appointment.Appointment(ts, int(ts), date_now, " This appointment is generated for test purpose.",
                                        "test_vac")
    test_app2 = Appointment.Appointment(ts, int(ts), date_of_last_app, " This appointment is generated for test purpose.",
                                        "test_vac")

    vet_operations.add_appointment(test_app1)
    vet_operations.add_appointment(test_app2)
    test_appointments = vet_operations.get_appointments_in_next_3days(int(ts))

    delete_query = """DELETE FROM appointment WHERE pet_ID = ? OR pet_ID = ?"""
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    cursor.execute(delete_query, (test_app1.pet_ID, test_app2.pet_ID))
    connection.commit()
    connection.close()

    assert test_appointments[0].pet_ID == test_app1.pet_ID and test_appointments[1].pet_ID == test_app2.pet_ID
