class Allergy:
    def __init__(self, id, pet_id, vet_ID, description, drugs):
        self.id = id  # id of the allergy
        self.pet_id = pet_id  # petID is the id of the pet that the allergy is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who diagnosed the allergy
        self.description = description  # description of the allergy
        self.drugs = drugs  # list of drugs in string format