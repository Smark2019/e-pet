import auth_operation
import vet_operations
from classes.Pet import Pet
from classes.Vaccination import Vaccination
from classes.Appointment import Appointment
from classes.Treatment import Treatment
from classes.Allergy import Allergy
import random
import sqlite3
from datetime import datetime, timedelta
from faker import Factory
from db import db_initialize


def get_random_user_id():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    getRandom = """SELECT * FROM user ORDER BY RANDOM() LIMIT 1"""
    cursor.execute(getRandom)
    random = cursor.fetchone()
    id = random[0]
    return id


def get_random_vet_and_pet_id():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    getRandomVet = """SELECT * FROM user where is_vet = 1 ORDER BY RANDOM() LIMIT 1"""
    getRandomPet = """SELECT * FROM pet ORDER BY RANDOM() LIMIT 1"""
    cursor.execute(getRandomVet)
    randomVet = cursor.fetchone()
    cursor.execute(getRandomPet)
    randomPet = cursor.fetchone()

    vet_id = randomVet[0]
    pet_id = randomPet[0]
    return vet_id, pet_id


def generateRandomDate():
    start_date = datetime(2007, 1, 1)
    end_date = datetime.today()

    # Generate a random date between the start and end dates

    random_date = start_date + (end_date - start_date) * random.random()
    return (random_date.strftime("%d-%m-%Y"))


def generateRandomDateAndTime():
    start_date = datetime(2007, 1, 1)
    end_date = datetime.today()

    # Generate a random date between the start and end dates

    random_date = start_date + (end_date - start_date) * random.random()
    return (random_date.strftime("%d-%m-%Y %H:%M"))


def generateRandomDateAndTimeForAppointment():

    start_date = datetime(2007, 1, 1)
    end_date = datetime.today()

    random_date = start_date + (end_date - start_date) * random.random()
    random_date = random_date.replace(
        hour=0, minute=0, second=0, microsecond=0)

    minSeconds = 32400  # 9am
    maxSeconds = 61200  # 5pm

    random_time = random_date + \
        timedelta(seconds=random.randint(minSeconds, maxSeconds))

    random_time = random_time.strftime("%d-%m-%Y %H:%M")

    return random_time
# Create a dataset of users


def add_users(count):
    firstNames = ["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack",
                  "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"]
    lastNames = ["Anderson", "Ashwoon", "Aikin", "Bateman", "Bongard", "Bowers", "Boyd", "Cannon", "Cast", "Deitz", "Dewalt", "Ebner", "Frick", "Hancock", "Haworth", "Hesch", "Hoffman", "Kassing", "Knutson", "Lawless", "Lawicki", "Mccord", "McCormack", "Miller", "Myers", "Nugent", "Ortiz", "Orwig", "Ory", "Paiser", "Pak", "Pettigrew", "Quinn", "Quizoz", "Ramachandran", "Resnick", "Sagar", "Schickowski", "Schiebel", "Sellon", "Severson", "Shaffer", "Solberg", "Soloman", "Sonderling", "Soukup", "Soulis", "Stahl", "Sweeney", "Tandy", "Trebil", "Trusela", "Trussel", "Turco", "Uddin", "Uflan", "Ulrich", "Upson", "Vader", "Vail", "Valente", "Van Zandt", "Vanderpoel", "Ventotla", "Vogal", "Wagle", "Wagner", "Wakefield", "Weinstein", "Weiss", "Woo", "Yang", "Yates", "Yocum", "Zeaser",
                 "Zeller", "Ziegler", "Bauer", "Baxster", "Casal", "Cataldi", "Caswell", "Celedon", "Chambers", "Chapman", "Christensen", "Darnell", "Davidson", "Davis", "DeLorenzo", "Dinkins", "Doran", "Dugelman", "Dugan", "Duffman", "Eastman", "Ferro", "Ferry", "Fletcher", "Fietzer", "Hylan", "Hydinger", "Illingsworth", "Ingram", "Irwin", "Jagtap", "Jenson", "Johnson", "Johnsen", "Jones", "Jurgenson", "Kalleg", "Kaskel", "Keller", "Leisinger", "LePage", "Lewis", "Linde", "Lulloff", "Maki", "Martin", "McGinnis", "Mills", "Moody", "Moore", "Napier", "Nelson", "Norquist", "Nuttle", "Olson", "Ostrander", "Reamer", "Reardon", "Reyes", "Rice", "Ripka", "Roberts", "Rogers", "Root", "Sandstrom", "Sawyer", "Schlicht", "Schmitt", "Schwager", "Schutz", "Schuster", "Tapia", "Thompson", "Tiernan", "Tisler"]
    mailDomains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@aol.com", "@ask.com",
                   "@live.com", "@mail.com", "@msn.com", "@passport.com", "@outlook.com"]
    countries = ["Romania", "Germany", "France", "Italy", "Spain", "United Kingdom", "Poland", "Netherlands", "Belgium", "Portugal", "Greece", "Czech Republic", "Hungary", "Sweden", "Austria", "Switzerland", "Denmark", "Finland", "Slovakia", "Norway", "Ireland", "Luxembourg", "Estonia", "Slovenia", "Lithuania", "Latvia", "Croatia", "Bulgaria", "Cyprus", "Malta", "Albania", "Moldova", "Bosnia and Herzegovina", "North Macedonia", "Serbia",
                 "Montenegro", "Kosovo", "Turkey", "Russia", "Ukraine", "Belarus", "Moldova", "Armenia", "Azerbaijan", "Georgia", "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan", "China", "India", "Indonesia", "Japan", "South Korea", "Malaysia", "Pakistan", "Philippines", "Thailand", "Vietnam", "Australia", "New Zealand", "Argentina", "Brazil", "Canada", "Chile", "Colombia", "Mexico", "Peru", "Venezuela", "South Africa", "Egypt"]
    cities = ["Bucharest", "Berlin", "Paris", "Rome", "Madrid", "London", "Warsaw", "Amsterdam", "Brussels", "Lisbon", "Athens", "Prague", "Budapest", "Stockholm", "Vienna", "Bern", "Copenhagen", "Helsinki", "Bratislava", "Oslo", "Dublin", "Luxembourg", "Tallinn", "Ljubljana", "Vilnius", "Riga", "Zagreb", "Sofia", "Nicosia", "Valletta", "Tirana", "Chisinau", "Sarajevo", "Skopje", "Belgrade", "Podgorica",
              "Pristina", "Ankara", "Moscow", "Kiev", "Minsk", "Chisinau", "Yerevan", "Baku", "Tbilisi", "Astana", "Bishkek", "Dushanbe", "Ashgabat", "Tashkent", "Beijing", "New Delhi", "Jakarta", "Tokyo", "Seoul", "Kuala Lumpur", "Islamabad", "Manila", "Bangkok", "Hanoi", "Canberra", "Wellington", "Buenos Aires", "Sao Paulo", "Ottawa", "Santiago", "Bogota", "Mexico City", "Lima", "Caracas", "Pretoria", "Cairo"]
    fake = Factory.create()

    vet_percentage = 0.05
    for i in range(count):
        nationalId = random.randint(10000000000, 99999999999)
        firstName = firstNames[random.randint(0, len(firstNames)-1)]
        lastName = lastNames[random.randint(0, len(lastNames)-1)]
        email = firstName + lastName + \
            str(random.randint(0, 1000)) + \
            mailDomains[random.randint(0, len(mailDomains)-1)]
        password = firstName.lower() + lastName.lower() + "123"
        phoneNumber = str(random.randint(100, 999)) + "-" + \
            str(random.randint(100, 999)) + "-" + \
            str(random.randint(1000, 9999))
        countryAndCity = random.randint(0, len(countries)-1)
        country = countries[countryAndCity]
        city = cities[countryAndCity]
        zipCode = str(random.randint(1000, 9999))
        address = fake.address()
        vetID = 0
        if (random.random() < vet_percentage):
            vetID = 1

        print("National ID => " + str(nationalId) + "- E-Mail => "+email + " - Password => " + password + " - First Name => " + firstName + " - Last Name => " +
              lastName + " - Phone Number => " + phoneNumber + " Address => " + address + " - Country => " + country + " - City => " + city + " - Zip Code => " + zipCode)
        auth_operation.register(nationalId, password, email, firstName,
                                lastName, phoneNumber, address, city, country, zipCode, vetID)


# Create a dataset of pets

def add_pets(count):

    petNames = ["Bella", "Lucy", "Molly", "Daisy", "Coco", "Charlie", "Milo", "Lola", "Max", "Buddy", "Bailey", "Rocky", "Toby", "Jack", "Jasper", "Oscar", "Teddy", "Lucky", "Maggie", "Lily", "Cody", "Gizmo", "Bear", "Harley", "Riley", "Duke", "Bentley", "Zeus", "Sam", "Loki", "Buster", "Rusty", "Baxter", "Cooper", "Murphy", "Louie", "George", "Bo", "Bandit", "Rocco", "Frankie", "Diesel", "Chico", "Ollie", "Romeo", "Henry", "Harley", "Rudy", "Bruno", "Rex", "Rufus", "Prince", "Sammy", "Ranger", "Rocco", "Scooter", "Jackson", "Gus", "Scout",
                "Moose", "Shadow", "Winston", "Copper", "Benny", "Joey", "Rusty", "Rudy", "Boomer", "Bubba", "Buck", "Buddy", "Casey", "Chance", "Chase", "Chester", "Chico", "Cody", "Dakota", "Dexter", "Diesel", "Duke", "Frankie", "Gizmo", "Gus", "Harley", "Henry", "Jack", "Jackson", "Jasper", "Joey", "Kobe", "Loki", "Louie", "Luke", "Mickey", "Milo", "Moose", "Murphy", "Ollie", "Oscar", "Prince", "Ranger", "Rex", "Rocco", "Romeo", "Rudy", "Rusty", "Sam", "Sammy", "Scout", "Shadow", "Simba", "Spike", "Tank", "Toby", "Tucker", "Winston", "Ziggy"]
    petSpecies = ["Dog", "Cat", "Bird", "Rabbit",
                  "Hamster", "Guinea Pig", "Ferret"]
    petGender = ["Male", "Female"]
    petSterilized = ["0", "1"]
    petHealthStatus = ["Healthy", "Sick", "Injured"]
    # get random petOwnerId from existing users in the database

    for i in range(count):

        pet_name = petNames[random.randint(0, len(petNames)-1)]
        pet_date_of_birth = generateRandomDate()
        pet_species = petSpecies[random.randint(0, len(petSpecies)-1)]
        pet_gender = petGender[random.randint(0, len(petGender)-1)]
        pet_sterilized = petSterilized[random.randint(
            0, len(petSterilized)-1)]
        pet_health_status = petHealthStatus[random.randint(
            0, len(petHealthStatus)-1)]
        pet_owner_id = get_random_user_id()
        print("Pet Name => " + pet_name + " - Pet Date Of Birth => " +
              pet_date_of_birth + " - Pet Species => " + pet_species)

        pet = Pet(pet_name, pet_date_of_birth, pet_species, pet_gender,
                  pet_sterilized, pet_health_status, pet_owner_id)
        vet_operations.add_pet(pet)


def add_vaccinations(count):
    vaccination_names = ['Distemper', 'Rabies',
                         'Parvovirus', 'Leptospirosis', 'Feline Leukemia']
    for i in range(count):
        randomCount = random.randint(1, 5)
        vet_ID, pet_ID = get_random_vet_and_pet_id()
        vaccination_name = vaccination_names[random.randint(
            0, len(vaccination_names)-1)]
        vaccination_date = generateRandomDate()
        vaccination_dose = random.randint(1, 20) * 10
        for j in range(randomCount):
            vaccination_date = datetime.strftime(datetime.strptime(
                vaccination_date, "%d-%m-%Y") + timedelta(days=30), "%d-%m-%Y")
            vaccination_count = j + 1
            print("Pet ID => " + str(pet_ID) + " Vet ID => " + str(vet_ID) + " - Vaccination Name => " + vaccination_name + " - Vaccination Date => " +
                  vaccination_date + " - Vaccination Dose => " + str(vaccination_dose) + " - Vaccination Count => " + str(vaccination_count))
            vet_operations.add_vaccination(Vaccination(
                pet_ID, vet_ID, vaccination_name, vaccination_date, vaccination_dose, vaccination_count))


def add_appointments(count):
    appointment_types = ['Vaccination', 'Checkup', 'Surgery', 'Other']
    vaccination_names = ['Distemper', 'Rabies',
                         'Parvovirus', 'Leptospirosis', 'Feline Leukemia']
    for i in range(count):
        vet_ID, pet_ID = get_random_vet_and_pet_id()
        date_of_appointment = generateRandomDateAndTimeForAppointment()
        appointment_description = appointment_types[random.randint(
            0, len(appointment_types)-1)]

        if appointment_description == "Vaccination":
            vaccination_name = vaccination_names[random.randint(
                0, len(vaccination_names)-1)]
        else:
            vaccination_name = ""

        print("Pet ID => " + str(pet_ID) + " Vet ID => " + str(vet_ID) + " - Appointment Date => " + date_of_appointment +
              " - Appointment Description => " + appointment_description + " - Vaccinations => " + vaccination_name)
        vet_operations.add_appointment(Appointment(
            pet_ID, vet_ID, date_of_appointment, appointment_description, vaccination_name))


def add_treatments(count):
    fake = Factory.create()
    medicines = ['Paracetamol', 'Ibuprofen', 'Aspirin', 'Cetirizine', 'Diphenhydramine', 'Loratadine', 'Prednisone', 'Prednisolone', 'Cortisone', 'Cortisol', 'Cyclosporine', 'Tacrolimus', 'Methylprednisolone', 'Methotrexate', 'Azathioprine',
                 'Mycophenolate', 'Cyclophosphamide', 'Methimazole', 'Carprofen', 'Meloxicam', 'Famotidine', 'Omeprazole', 'Metoclopramide', 'Dexamethasone', 'Doxycycline', 'Amoxicillin', 'Clindamycin', 'Metronidazole', 'Enrofloxacin', 'Flucon']
    for i in range(count):
        vet_ID, pet_ID = get_random_vet_and_pet_id()
        treatment_description = fake.text()
        # pick random medicines
        pick3Medicines = random.sample(medicines, 3)
        randomNum = random.randint(0, len(pick3Medicines)-1)
        used_medicine = ""
        for j in range(randomNum - 1):
            used_medicine = used_medicine + pick3Medicines[j] + ", "
        used_medicine = used_medicine + pick3Medicines[randomNum]

        treatment_date = generateRandomDateAndTimeForAppointment()

        print("Pet ID => " + str(pet_ID) + " Vet ID => " + str(vet_ID) + " - Treatment Description => " +
              treatment_description + " - Used Medicine => " + used_medicine + " - Treatment Date => " + treatment_date)
        vet_operations.add_treatment(Treatment(
            pet_ID, vet_ID, treatment_description, used_medicine, treatment_date))


def add_allergies(count):
    medicines = ['Paracetamol', 'Ibuprofen', 'Aspirin', 'Cetirizine', 'Diphenhydramine', 'Loratadine', 'Prednisone', 'Prednisolone', 'Cortisone', 'Cortisol', 'Cyclosporine', 'Tacrolimus', 'Methylprednisolone', 'Methotrexate', 'Azathioprine',
                 'Mycophenolate', 'Cyclophosphamide', 'Methimazole', 'Carprofen', 'Meloxicam', 'Famotidine', 'Omeprazole', 'Metoclopramide', 'Dexamethasone', 'Doxycycline', 'Amoxicillin', 'Clindamycin', 'Metronidazole', 'Enrofloxacin', 'Flucon']
    allergyNames = ['Allergic Rhinitis', 'Allergic Conjunctivitis', 'Allergic Asthma', 'Allergic Dermatitis', 'Allergic Urticaria', 'Allergic Angioedema', 'Allergic Gastroenteritis', 'Allergic Shock', 'Allergic Anaphylaxis', 'Allergic Rhinosinusitis', 'Allergic Bronchitis', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis',
                    'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis', 'Allergic Bronchopulmonary Mycosis', 'Allergic Bronchopulmonary Fungal Infections', 'Allergic Bronchopulmonary Aspergillosis']
    for i in range(count):
        vet_ID, pet_ID = get_random_vet_and_pet_id()
        description = random.choice(allergyNames)

        pick3Medicines = random.sample(medicines, 3)
        randomNum = random.randint(0, len(pick3Medicines)-1)

        drugs = ""
        for j in range(randomNum - 1):
            drugs = drugs + pick3Medicines[j] + ", "
        drugs = drugs + pick3Medicines[randomNum]

        print("Pet ID => " + str(pet_ID) + " Vet ID => " + str(vet_ID) +
              " Description => " + description + " Drugs => " + drugs)
        vet_operations.add_allergy(Allergy(pet_ID, vet_ID, description, drugs))


def generate_fake_dataset(count):
    db_initialize.initialize_db()
    add_users(count)
    add_pets(int(count * 1.5))
    add_vaccinations(int(count * 2))
    add_appointments(int(count * 3))
    add_allergies(int(count * 1.5))
    add_treatments(int(count * 3))


if __name__ == "__main__":
    print("Creating Dataset...")
    generate_fake_dataset(100)
