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
        id integer primary key autoincrement,
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
        id integer primary key autoincrement,
        pet_ID integer,
        vet_ID integer,
        name text,
        date_of_vaccination text,
        dose_given real,
        count integer
        )
        """

    appointment_table_query = """CREATE TABLE IF NOT EXISTS appointment(
        id integer primary key autoincrement,
        pet_ID integer,
        vet_ID integer,
        date_of_appointment text,
        description text,
        vaccinations text
        )
        """

    treatment_table_query = """CREATE TABLE IF NOT EXISTS treatment(
        id integer primary key autoincrement,
        pet_ID integer,
        vet_ID integer,
        description text
        used_medicine text,
        date_of_treatment text,
        )
        """

    allergy_table_query = """CREATE TABLE IF NOT EXISTS allergy(
        id integer primary key autoincrement,
        pet_ID integer,
        vet_ID integer,
        description integer,
        drugs text,
        )
        """

    cursor.execute(user_table_query)
    cursor.execute(pet_table_query)
    cursor.execute(vaccination_table_query)
    cursor.execute(appointment_table_query)
    cursor.execute(treatment_table_query)
    cursor.execute(allergy_table_query)

    connection.commit()
