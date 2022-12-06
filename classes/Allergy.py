class Allergy:
    def __init__(self, pet_ID, vet_ID, description, drugs, id=-1):
        self.pet_ID = pet_ID  # petID is the id of the pet that the allergy is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who diagnosed the allergy
        self.description = description  # description of the allergy
        self.drugs = drugs  # list of drugs in string format
        self.id = id  # id of the allergy
        
    def to_string(self):
        return "Allergy ID: " + str(self.id) + " Pet ID: " + str(self.pet_ID) + " Vet ID: " + str(self.vet_ID) + " Description: " + self.description + " Drugs: " + self.drugs
