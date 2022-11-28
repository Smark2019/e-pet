import sqlite3
import hashlib

def authentification(id, password):
    
    """_summary_ : Authenticates the user and logs them in if the credentials are correct.

    Args:
        id (int): The id of the user.
        password (String): The password of the user in hashed form.

    Returns:
        int: 1 if the user is authenticated, 0 if the password is wrong, -1 if the user doesn't exist.
    """
    
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        user = cursor.fetchone()
        
        if user[1] == password: #user[1] is the password column in the database
            return 1 #Login successful
        else:
            return 0 #Wrong password
    except Exception as err:
        print(err)
    
    connection.close()
    return -1 #Wrong ID or password

def register(id, password, email, name, surname, phone, address, city, country, zip_code, is_vet): #register function for the register page to use when the user clicks the register button
    
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    try:
        cursor.execute("INSERT INTO users(id, password, email, name, surname, phone, address, city, country, zip_code, is_vet) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, password, email, name, surname, phone, address, city, country, zip_code, is_vet))
        connection.commit()
    except Exception as err:
        print(err)
        
    connection.close()