import vet_operations
from classes import Pet, Vaccination, Appointment, Treatment, Allergy
import datetime
import sqlite3

# Pytest is used to run the test run with python -m pytest


def test_invalid_search_pet():
    assert vet_operations.search_pet(123123123123) == -1


def test_able_to_add_pet():
    test_pet = Pet.Pet("Olive", "12.12.2021", "Dog",
                       "Male", "No", "Healthy", "12345", 1)
    assert vet_operations.add_pet(test_pet)
    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM pet WHERE id = '12345' """
    cursor.execute(get_added_pet)
    result = cursor.fetchone()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    return test_pet.id == result[0]


def test_edit_pet():
    test_pet = Pet.Pet("Olive", "12.12.2021",
                       "Dog", "Male", "No", "Healthy", "12345", 1)

    vet_operations.edit_pet(test_pet.id, "Yes",
                            "Not Healthy", test_pet.owner_ID)

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM pet WHERE id = ? """
    cursor.execute(get_added_pet, (test_pet.id,))
    result = cursor.fetchone()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    return result[5] == "Yes" and result[6] == "Not Healthy"


def test_add_vaccination():

    test_vac = Vaccination.Vaccination("12345", "345",
                                       "HPP-B", "7.12.2022", "1.5 Mg", "1", 11)
    vet_operations.add_vaccination(test_vac)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM vaccination WHERE id = ? """
    cursor.execute(get_added_pet, (test_vac.id,))
    result = cursor.fetchone()
    connection.close()
    return result[0] == test_vac.id


def test_add_appointment():
    test_app = Appointment.Appointment("12345", 11, "12.12.2022", " This appointment is generated for test purpose.",
                                       "test_vac")
    vet_operations.add_appointment(test_app)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM appointment WHERE id = ? """
    cursor.execute(get_added_pet, (test_app.id,))
    result = cursor.fetchone()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    return result[0] == test_app.id


def test_add_treatment():
    test_treat = Treatment.Treatment(
        "12345", "11", "This treatment is generated for test purpose.", "Apoquel Tablets for Dogs", "12.12.2022", 11)
    vet_operations.add_treatment(test_treat)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM appointment WHERE id = ? """
    cursor.execute(get_added_pet, (test_treat.id,))
    result = cursor.fetchone()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    return result[0] == test_treat.id


def test_add_allergy():
    test_allergy = Allergy.Allergy("12345", "11", "This allergy is generated for test purpose. ",
                                   "No Medicine", 1)
    vet_operations.add_allergy(test_allergy)

    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet = """SELECT * FROM allergy WHERE id = ? """
    cursor.execute(get_added_pet, (test_allergy.id,))
    result = cursor.fetchone()
    connection.close()
    # maybe other attributes shall be checked. later on we back.
    return result[0] == test_allergy.id


def test_get_appointments_in_next_3days():
    test_appointments = vet_operations.get_appointments_in_next_3days("11")
    most_close_date = datetime.datetime.strptime(
        test_appointments[0][3], "%d-%m-%Y %H:%M")
    most_far_date = datetime.datetime.strptime(
        test_appointments[len(test_appointments)-1][3], "%d-%m-%Y %H:%M")
    assert most_close_date - most_far_date == 3
