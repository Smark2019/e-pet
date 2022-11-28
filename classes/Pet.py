class Pet:
    def __init__(self, id, name, date_of_birth, species, gender, sterility,health_status,owner_ID,vaccination_list,appointment_list,treatment_list,allergie_list):
        self.id = id #id of the pet
        self.name = name #name of the pet
        self.date_of_birth = date_of_birth #date of birth of the pet in datetime format
        self.species = species #species of the pet 
        self.gender = gender #gender of the pet
        self.sterility = sterility #sterility of the pet in boolean format
        self.health_status = health_status #health status of the pet in string format
        self.owner_ID = owner_ID #ownerID is the id of the owner of the pet
        self.vaccination_list = vaccination_list #a list which contains vaccination objects
        self.appointment_list = appointment_list #a list which contains appointment objects
        self.treatment_list = treatment_list #a list which contains treatment objects
        self.allergie_list = allergie_list #a list which contains allergy objects
