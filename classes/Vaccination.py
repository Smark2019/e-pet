class Vaccination():
    
    def __init__(self, id, name, date_of_vaccination, pet_ID, vet_ID, dose_given,count):
        self.id = id #id of the vaccination
        self.name = name #name of the vaccination
        self.date_of_vaccination = date_of_vaccination #date of vaccination in datetime format
        self.pet_ID = pet_ID #petID is the id of the pet that the vaccination is for
        self.vet_ID = vet_ID #vetID is the id of the vet who vaccinated the pet
        self.dose_given = dose_given #dose given of the vaccination in float format
        self.count = count #count of the vaccination in integer format
        