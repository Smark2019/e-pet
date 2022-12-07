import vet_operations
from classes import Pet, Vaccination, Appointment, Treatment, Allergy
import datetime
import sqlite3
import pet_owner_operations
# Pytest is used to run the test run with python -m pytest


def test_get_list_of_pets():
    test_pet = Pet.Pet("Olive","12.12.2021","Dog","Male","No"
    ,"Healthy","12345",1)
    
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    pet_add_query = """INSERT INTO pet(name,date_of_birth,species,gender,sterility,health_status,owner_ID) VALUES(?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(pet_add_query, (test_pet.name, test_pet.date_of_birth,
                   test_pet.species, test_pet.gender, test_pet.sterility, test_pet.health_status, test_pet.owner_ID))

    connection.commit()
    connection.close()
    test_pet_list = pet_owner_operations.get_list_of_pets(test_pet.owner_ID)
    assert test_pet_list[0].id == test_pet.id

