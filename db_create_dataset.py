import auth_operation
import vet_operations
from classes.Pet import Pet
from classes.Vaccination import Vaccination
from classes.Appointment import Appointment
from classes.Treatment import Treatment
from classes.Allergy import Allergy
import random

# Create a dataset of pets

""" for i in range(1, 5):
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
        Allergy(i, 2, "description", "drugs")) """

# Create a dataset of users

def add_user(count):
    firstNames = ["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"]
    lastNames = ["Anderson", "Ashwoon", "Aikin", "Bateman", "Bongard", "Bowers", "Boyd", "Cannon", "Cast", "Deitz", "Dewalt", "Ebner", "Frick", "Hancock", "Haworth", "Hesch", "Hoffman", "Kassing", "Knutson", "Lawless", "Lawicki", "Mccord", "McCormack", "Miller", "Myers", "Nugent", "Ortiz", "Orwig", "Ory", "Paiser", "Pak", "Pettigrew", "Quinn", "Quizoz", "Ramachandran", "Resnick", "Sagar", "Schickowski", "Schiebel", "Sellon", "Severson", "Shaffer", "Solberg", "Soloman", "Sonderling", "Soukup", "Soulis", "Stahl", "Sweeney", "Tandy", "Trebil", "Trusela", "Trussel", "Turco", "Uddin", "Uflan", "Ulrich", "Upson", "Vader", "Vail", "Valente", "Van Zandt", "Vanderpoel", "Ventotla", "Vogal", "Wagle", "Wagner", "Wakefield", "Weinstein", "Weiss", "Woo", "Yang", "Yates", "Yocum", "Zeaser", "Zeller", "Ziegler", "Bauer", "Baxster", "Casal", "Cataldi", "Caswell", "Celedon", "Chambers", "Chapman", "Christensen", "Darnell", "Davidson", "Davis", "DeLorenzo", "Dinkins", "Doran", "Dugelman", "Dugan", "Duffman", "Eastman", "Ferro", "Ferry", "Fletcher", "Fietzer", "Hylan", "Hydinger", "Illingsworth", "Ingram", "Irwin", "Jagtap", "Jenson", "Johnson", "Johnsen", "Jones", "Jurgenson", "Kalleg", "Kaskel", "Keller", "Leisinger", "LePage", "Lewis", "Linde", "Lulloff", "Maki", "Martin", "McGinnis", "Mills", "Moody", "Moore", "Napier", "Nelson", "Norquist", "Nuttle", "Olson", "Ostrander", "Reamer", "Reardon", "Reyes", "Rice", "Ripka", "Roberts", "Rogers", "Root", "Sandstrom", "Sawyer", "Schlicht", "Schmitt", "Schwager", "Schutz", "Schuster", "Tapia", "Thompson", "Tiernan", "Tisler" ]
    mailDomains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@aol.com", "@ask.com", "@live.com", "@mail.com", "@msn.com", "@passport.com", "@outlook.com"]
    
    for i in range(count):
        firstName = firstNames[random.randint(0, len(firstNames)-1)]
        lastName = lastNames[random.randint(0, len(lastNames)-1)]
        email = firstName + lastName + str(random.randint(0, 1000)) + mailDomains[random.randint(0, len(mailDomains)-1)]
        password = firstName.lower() + lastName.lower() + "123"
        phoneNumber = str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))
        print("E-Mail => "+email + " Password => " +  password + " First Name => " + firstName + " Last Name => "+ lastName + " Phone Number => " + phoneNumber)



add_user(4)

    


    
