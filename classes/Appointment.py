class Appointment:
    def __init__(self, id,vet_ID,pet_ID, date_of_appointment, description, vaccinations):
        self.id = id #id of the appointment
        self.vet_ID = vet_ID #vetID is the id of the vet who made the appointment
        self.pet_ID = pet_ID #petID is the id of the pet that the appointment is for
        self.date_of_appointment = date_of_appointment #date of appointment in datetime format
        self.description = description #description of the appointment
        self.vaccinations = vaccinations #list of vaccinations in string format