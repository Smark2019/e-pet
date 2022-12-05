import auth_operation
import vet_operations
from classes.Pet import Pet
from classes.Vaccination import Vaccination
from classes.Appointment import Appointment
from classes.Treatment import Treatment
from classes.Allergy import Allergy
import random
import sqlite3

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
    countries = ["Romania", "Germany", "France", "Italy", "Spain", "United Kingdom", "Poland", "Netherlands", "Belgium", "Portugal", "Greece", "Czech Republic", "Hungary", "Sweden", "Austria", "Switzerland", "Denmark", "Finland", "Slovakia", "Norway", "Ireland", "Luxembourg", "Estonia", "Slovenia", "Lithuania", "Latvia", "Croatia", "Bulgaria", "Cyprus", "Malta", "Albania", "Moldova", "Bosnia and Herzegovina", "North Macedonia", "Serbia", "Montenegro", "Kosovo", "Turkey", "Russia", "Ukraine", "Belarus", "Moldova", "Armenia", "Azerbaijan", "Georgia", "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan", "China", "India", "Indonesia", "Japan", "South Korea", "Malaysia", "Pakistan", "Philippines", "Thailand", "Vietnam", "Australia", "New Zealand", "Argentina", "Brazil", "Canada", "Chile", "Colombia", "Mexico", "Peru", "Venezuela", "South Africa", "Egypt"]
    cities = ["Bucharest", "Berlin", "Paris", "Rome", "Madrid", "London", "Warsaw", "Amsterdam", "Brussels", "Lisbon", "Athens", "Prague", "Budapest", "Stockholm", "Vienna", "Bern", "Copenhagen", "Helsinki", "Bratislava", "Oslo", "Dublin", "Luxembourg", "Tallinn", "Ljubljana", "Vilnius", "Riga", "Zagreb", "Sofia", "Nicosia", "Valletta", "Tirana", "Chisinau", "Sarajevo", "Skopje", "Belgrade", "Podgorica", "Pristina", "Ankara", "Moscow", "Kiev", "Minsk", "Chisinau", "Yerevan", "Baku", "Tbilisi", "Astana", "Bishkek", "Dushanbe", "Ashgabat", "Tashkent", "Beijing", "New Delhi", "Jakarta", "Tokyo", "Seoul", "Kuala Lumpur", "Islamabad", "Manila", "Bangkok", "Hanoi", "Canberra", "Wellington", "Buenos Aires", "Sao Paulo", "Ottawa", "Santiago", "Bogota","Mexico City", "Lima", "Caracas", "Pretoria", "Cairo"]
    streetNames = ["Main", "2nd", "1st", "Park", "Oak", "Pine", "Elm", "Maple", "Cedar", "Washington", "Lake", "Hill", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st", "32nd", "33rd", "34th", "35th", "36th", "37th", "38th", "39th", "40th", "41st", "42nd", "43rd", "44th", "45th", "46th", "47th", "48th", "49th", "50th", "51st", "52nd", "53rd", "54th", "55th", "56th", "57th", "58th", "59th", "60th", "61st", "62nd", "63rd", "64th", "65th", "66th", "67th", "68th", "69th", "70th", "71st", "72nd", "73rd", "74th", "75th", "76th", "77th", "78th", "79th", "80th", "81st", "82nd", "83rd", "84th", "85th", "86th", "87th", "88th", "89th", "90th", "91st", "92nd", "93rd", "94th", "95th", "96th", "97th", "98th", "99th", "100th", "101st", "102nd", "103rd", "104th", "105th", "106th", "107th", "108th", "109th", "110th", "111th", "112th", "113th", "114th", "115th", "116th", "117th"]
    for i in range(count):
        nationalId = random.randint(10000000000, 99999999999)
        firstName = firstNames[random.randint(0, len(firstNames)-1)]
        lastName = lastNames[random.randint(0, len(lastNames)-1)]
        email = firstName + lastName + str(random.randint(0, 1000)) + mailDomains[random.randint(0, len(mailDomains)-1)]
        password = firstName.lower() + lastName.lower() + "123"
        phoneNumber = str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))
        countryAndCity = random.randint(0, len(countries)-1)
        country = countries[countryAndCity]
        city = cities[countryAndCity]
        zipCode = str(random.randint(1000, 9999))
        address = str(random.randint(1, 100)) + " " + streetNames[random.randint(0, len(streetNames)-1)] + " St."
        
        print("National ID => "+ str(nationalId)+ "- E-Mail => "+email + " - Password => " +  password + " - First Name => " + firstName + " - Last Name => "+ lastName + " - Phone Number => " + phoneNumber + " Address => " + address + " - Country => " + country + " - City => " + city + " - Zip Code => " + zipCode)
        auth_operation.register(nationalId, password,email, firstName, lastName, phoneNumber, address, city,country , zipCode, 0)


# Create a dataset of pets



    


    
