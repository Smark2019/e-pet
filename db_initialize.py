import sqlite3


def initialize_db():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()

    user_table_query = """CREATE TABLE IF NOT EXISTS users(
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

    pet_table_query = """CREATE TABLE IF NOT EXISTS pet(
        id integer primary key,
        name text,
        date_of_birth text,
        species text,
        gender text,
        sterility integer,
        health_status text,
        owner_ID integer,
       )
        """

    vaccination_table_query = """CREATE TABLE IF NOT EXISTS vaccination(
        id integer primary key,
        name text,
        date_of_vaccination text,
        pet_ID integer,
        vet_ID integer,
        dose_given real,
        count integer
        )
        """

    appointment_table_query = """CREATE TABLE IF NOT EXISTS appointment(
        id integer primary key,
        vet_ID integer,
        pet_ID integer,
        date_of_appointment text,
        description text,
        vaccinations text
        )
        """

    treatment_table_query = """CREATE TABLE IF NOT EXISTS treatment(
        id integer primary key,
        vet_ID integer,
        description text
        used_medicine text,
        date_of_treatment text,
        pet_ID integer,
        )
        """

    allergie_table_query = """CREATE TABLE IF NOT EXISTS allergie(
        id integer primary key,
        description integer,
        vet_ID integer,
        drugs text,
        )
        """

    cursor.execute(user_table_query)
    cursor.execute(pet_table_query)
    cursor.execute(vaccination_table_query)
    cursor.execute(appointment_table_query)
    cursor.execute(treatment_table_query)
    cursor.execute(allergie_table_query)

    connection.commit()
