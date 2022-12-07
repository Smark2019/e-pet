import vet_operations
from classes import Pet
import sqlite3

# Pytest is used to run the test run with python -m pytest


def test_invalid_search_pet():
    assert vet_operations.search_pet(123123123123) == -1


def test_able_to_add_pet():
    test_pet = Pet.Pet("Olive","12.12.2021","Dog","Male","No","Healthy","12345",1)
    assert vet_operations.add_pet(test_pet)
    # here db query should work:
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet ="""SELECT * FROM pet WHERE id = '12345' """
    cursor.execute(get_added_pet)
    result = cursor.fetchone()
    connection.close()
    return test_pet.id == result[0] # maybe other attributes shall be checked. later on we back.

def test_edit_pet():
    test_pet = Pet.Pet("Olive","12.12.2021",
    "Dog","Male","No","Healthy","12345",1)
    
    vet_operations.edit_pet(test_pet.id,"Yes",
    "Not Healthy",test_pet.owner_ID)

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    get_added_pet ="""SELECT * FROM pet WHERE id = ? """
    cursor.execute(get_added_pet, (test_pet.id,))
    result = cursor.fetchone()
    connection.close()
    return result[5] == "Yes" and result[6] == "Not Healthy"
    





if __name__ == "__main__":
    test_able_to_add_pet()

