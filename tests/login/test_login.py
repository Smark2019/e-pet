import auth_operation
import time
import hashlib

# Pytest is used to run the test


def test_login_response_time():

    start_time = time.time()
    auth_operation.authentification(
        12, hashlib.sha256("1231".encode('utf-8')).hexdigest())
    end_time = time.time()
    assert end_time - start_time < 5


def test_login_wrong_id():
    assert auth_operation.authentification(
        123123123123, hashlib.sha256("1231".encode('utf-8')).hexdigest()) == -1
