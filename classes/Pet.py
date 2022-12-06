class Pet:
    vaccination_list = []  # a list which contains vaccination objects
    appointment_list = []  # a list which contains appointment objects
    treatment_list = []  # a list which contains treatment objects
    allergie_list = []  # a list which contains allergy objects

    def __init__(self,name, date_of_birth, species, gender, sterility, health_status, owner_ID,id= -1):
        self.name = name  # name of the pet
        self.date_of_birth = date_of_birth  # date of birth of the pet in datetime format
        self.species = species  # species of the pet
        self.gender = gender  # gender of the pet
        self.sterility = sterility  # sterility of the pet in boolean format
        self.health_status = health_status  # health status of the pet in string format
        self.owner_ID = owner_ID  # ownerID is the id of the owner of the pet
        self.id = id  # id of the pet

    def to_string(self):
        return "Pet ID: " + str(self.id) + " Name: " + self.name + " Date of Birth: " + str(self.date_of_birth) + " Species: " + self.species + " Gender: " + self.gender + " Sterility: " + str(self.sterility) + " Health Status: " + self.health_status + " Owner ID: " + str(self.owner_ID)
