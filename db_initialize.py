import sqlite3


def initialize_db():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    userTableQuery = """CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        password text,
        email text,
        name text,
        surname text,
        phone text,
        address text,
        city text,
        country text,
        zip_code text,
        is_vet integer)
        """

    petTableQuery = """CREATE TABLE IF NOT EXISTS pet(
        id integer primary key,
        name text,
        date_of_birth text,
        species text,
        gender text,
        sterility integer,
        health_status text,
        owner_ID integer,
        vaccination_list text,
        appointment_list text,
        treatment_list text,
        allergie_list text
       )
        """

    vaccinationTableQuery = """CREATE TABLE IF NOT EXISTS vaccination(
        id integer primary key,
        name text,
        date_of_vaccination text,
        pet_ID integer,
        vet_ID integer,
        dose_given real,
        count integer
        )
        """

    appointmentTableQuery = """CREATE TABLE IF NOT EXISTS appointment(
        id integer primary key,
        vet_ID integer,
        pet_ID integer,
        date_of_appointment text,
        description text,
        vaccinations text
        )
        """

    treatmentTableQuery = """CREATE TABLE IF NOT EXISTS treatment(
        id integer primary key,
        vet_ID integer,
        pet_ID integer,
        used_medicine text,
        date_of_treatment text,
        description text
        )
        """

    allergieTableQuery = """CREATE TABLE IF NOT EXISTS allergie(
        id integer primary key,
        description integer,
        vet_ID integer,
        drugs text,
        )
        """

    cursor.execute(userTableQuery)
    cursor.execute(petTableQuery)
    cursor.execute(vaccinationTableQuery)
    cursor.execute(appointmentTableQuery)
    cursor.execute(treatmentTableQuery)
    cursor.execute(allergieTableQuery)

    connection.commit()
