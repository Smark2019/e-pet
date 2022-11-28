class Treatment:
    def __init__(self, id, vet_ID, pet_ID, used_medicine, date_of_treatment, description ):
        self.id = id # id of the treatment
        self.vet_ID = vet_ID #vetID is the id of the vet who treated the pet
        self.description = description #description of the treatment
        self.used_medicine = used_medicine #list of medicine in string format
        self.date_of_treatment = date_of_treatment #date of treatment in datetime format
        self.pet_ID = pet_ID #petID is the id of the pet that the treatment is for