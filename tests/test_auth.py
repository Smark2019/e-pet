import auth_operation
import time
import hashlib
import sqlite3

# Pytest is used to run the test run with python -m pytest


def unblock_user(id):
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    cursor.execute("UPDATE user SET blocked_date = ? WHERE id = ?", (None, id))
    cursor.execute("UPDATE user SET login_attempts = 0 WHERE id = ?", (id,))
    connection.commit()
    connection.close()


def get_random_user_credentials():
    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    getRandom = """SELECT * FROM user ORDER BY RANDOM() LIMIT 1"""
    cursor.execute(getRandom)
    random = cursor.fetchone()
    id = random[0]
    password = random[1]
    return id, password


def test_login_response_time():
    id, password = get_random_user_credentials()
    start_time = time.time()
    auth_operation.authentification(
        id, password)
    end_time = time.time()
    assert end_time - start_time < 5


def test_login_wrong_id():
    assert auth_operation.authentification(
        123123123123, hashlib.sha256("1231".encode('utf-8')).hexdigest()) == -1


def test_successful_login():
    id, password = get_random_user_credentials()
    assert auth_operation.authentification(
        id, password) == 1


def test_user_block_for_unsuccessful_login():
    id, password = get_random_user_credentials()
    for i in range(4):
        auth_operation.authentification(
            id, hashlib.sha256("1231".encode('utf-8')).hexdigest())

    login_status = auth_operation.authentification(id, hashlib.sha256(
        "1231".encode('utf-8')).hexdigest())

    unblock_user(id)

    assert login_status == -2 or -3
