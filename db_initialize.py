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
    cursor.execute(userTableQuery) 
    connection.commit()
    