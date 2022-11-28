class Vaccination():

    def __init__(self, id, vet_ID, pet_ID, name, date_of_vaccination, dose_given, count):
        self.id = id  # id of the vaccination
        self.vet_ID = vet_ID  # vetID is the id of the vet who vaccinated the pet
        self.pet_ID = pet_ID  # petID is the id of the pet that the vaccination is for
        self.name = name  # name of the vaccination
        # date of vaccination in datetime format
        self.date_of_vaccination = date_of_vaccination
        self.dose_given = dose_given  # dose given of the vaccination in float format
        self.count = count  # count of the vaccination in integer format
