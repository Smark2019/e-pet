class Treatment:
    def __init__(self, pet_ID, vet_ID,description, used_medicine, date_of_treatment ):
        self.pet_ID = pet_ID  # petID is the id of the pet that the treatment is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who treated the pet
        self.description = description  # description of the treatment
        self.used_medicine = used_medicine  # list of medicine in string format
        # date of treatment in datetime format
        self.date_of_treatment = date_of_treatment

    def to_string(self):
        return "Treatment ID: " + str(self.id) + " Pet ID: " + str(self.pet_ID) + " Vet ID: " + str(self.vet_ID) + " Date of Treatment: " + str(self.date_of_treatment) + " Description: " + self.description + " Used Medicine: " + self.used_medicine
