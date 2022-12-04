import auth_operation
import vet_operations
from classes.Pet import Pet
from classes.Vaccination import Vaccination
from classes.Appointment import Appointment
from classes.Treatment import Treatment
from classes.Allergy import Allergy

# Create a dataset of users


auth_operation.register(1, "131", "gmail", "durmus",
                        "berk", "123", "asd", "asdf", "asdfg", 1234, 0, None, 0)
auth_operation.register(2, "231", "gmail", "selim", "cavas",
                        "123", "asd", "asdf", "asdfg", 1234, 1, None, 0)
auth_operation.register(3, "331", "gmail", "metin", "berk",
                        "123", "asd", "asdf", "asdfg", 1234, 0, None, 0)
auth_operation.register(4, "431", "gmail", "selim", "berk",
                        "123", "asd", "asdf", "asdfg", 1234, 1, None, 0)

# Create a dataset of pets

for i in range(1, 5):
    vet_operations.add_pet(Pet("dog1", "2020-01-01", "labrador",
                               "male", "sterile", "healthy", 1))

# Create a dataset of appointments

for i in range(1, 5):
    vet_operations.add_appointment(
        Appointment(i, 2, "2020-01-01", "test", "vaccination"))

# Create a dataset of vaccinations

for i in range(1, 5):
    vet_operations.add_vaccination(
        Vaccination(i, 2, "name", "2020-01-01", 0.5, 1))

# Create a dataset of treatments

for i in range(1, 5):
    vet_operations.add_treatment(
        Treatment(i, 2, "description", "medicine", "2020-01-01"))

# Create a dataset of allergies

for i in range(1, 5):
    vet_operations.add_allergy(
        Allergy(i, 2, "description", "drugs"))
