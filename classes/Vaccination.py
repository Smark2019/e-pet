class Vaccination():

    def __init__(self, pet_ID, vet_ID, name, date_of_vaccination, dose_given, count, id=-1):
        self.pet_ID = pet_ID  # petID is the id of the pet that the vaccination is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who vaccinated the pet
        self.name = name  # name of the vaccination
        # date of vaccination in datetime format
        self.date_of_vaccination = date_of_vaccination
        self.dose_given = dose_given  # dose given of the vaccination in float format
        self.count = count  # count of the vaccination in integer format
        self.id = id  # id of the vaccination
        
    def to_string(self):
        return "Vaccination ID: " + str(self.id) + " Pet ID: " + str(self.pet_ID) + " Vet ID: " + str(self.vet_ID) + " Name: " + self.name + " Date of Vaccination: " + str(self.date_of_vaccination) + " Dose Given: " + str(self.dose_given) + " Count: " + str(self.count)
