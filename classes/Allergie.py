class Allergie:
    def __init__(self, id, description, vet_ID, drugs):
        self.id = id #id of the allergy
        self.description = description #description of the allergy
        self.vet_ID = vet_ID #vetID is the id of the vet who diagnosed the allergy
        self.drugs = drugs #list of drugs in string format
        