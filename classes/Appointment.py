class Appointment:
    def __init__(self, pet_ID, vet_ID, date_of_appointment, description, vaccinations, id = -1):
        self.pet_ID = pet_ID  # petID is the id of the pet that the appointment is for
        self.vet_ID = vet_ID  # vetID is the id of the vet who made the appointment
        self.date_of_appointment = date_of_appointment # date of appointment in datetime format
        self.description = description  # description of the appointment
        self.vaccinations = vaccinations  # list of vaccinations in string format
        self.id = id  # id of the appointment

    def to_string(self):
        return "Appointment ID: " + str(self.id) + " Pet ID: " + str(self.pet_ID) + " Vet ID: " + str(self.vet_ID) + " Date of Appointment: " + str(self.date_of_appointment) + " Description: " + self.description + " Vaccinations: " + self.vaccinations
