class Appointment:
    def __init__(self, id, pet_ID, vet_ID, date_of_appointment, description, vaccinations):
        self.id = id  # id of the appointment
        self.pet_ID = pet_ID  # petID is the id of the pet that the appointment is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who made the appointment
        # date of appointment in datetime format
        self.date_of_appointment = date_of_appointment
        self.description = description  # description of the appointment
        self.vaccinations = vaccinations  # list of vaccinations in string format
