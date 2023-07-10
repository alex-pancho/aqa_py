from hillel_api import *
import pytest


@pytest.fixture
def sign_up_positive():
    """sign up with valid data"""
    data = {
        "name": "Leonel",
        "lastName": "Messi",
        "email": "messibarcelona6@test.com",
        "password": "Qwerty12345",
        "repeatPassword": "Qwerty12345"
    }

    r = auth.signup(s, data)
    return r.status_code

def test_sign_up_positive(sign_up_positive):
    """test for status code, sign up with valid data"""
    assert sign_up_positive == 201, f"Something goes wrong. Status code {sign_up_positive} is not equal 201"



@pytest.fixture
def sign_in_positive():
    """sign in with valid data"""
    data = {
        "email": "messibarcelona6@test.com",
        "password": "Qwerty12345",
        "remember": False
    }

    r = auth.signin(s, data)
    return r.status_code

def test_sign_in_positive(sign_in_positive):
    """test status code, sign in with valid data"""
    assert sign_in_positive == 200, f"Something goes wrong. Status code {sign_in_positive} is not equal 200"



@pytest.fixture
def reset_password_wrong_email_status_code():
    """reset password with wrong email, function return status code"""
    data = {
        "email": "essibarcelona1@test.com"
    }

    r = auth.resetpassword(s, data)
    return r.status_code

def test_reset_password_wrong_email_status_code(reset_password_wrong_email_status_code):
    """test status code , reset password with wrong email"""
    assert reset_password_wrong_email_status_code == 400, "Please, check your email"



@pytest.fixture
def reset_password_wrong_email_json():
    """reset password with wrong email, function return json"""
    data = {
        "email": "essibarcelona1@test.com"
    }

    r = auth.resetpassword(s, data)
    r_json = after_processsing(r)
    return r_json

def test_reset_password_wrong_email_json(reset_password_wrong_email_json):
    """test 'status' and 'message', reset password with wrong email"""
    assert reset_password_wrong_email_json["status"] == "error", "'status' should be 'error'"
    assert reset_password_wrong_email_json["message"] == "Bad request", "'message' should be 'Bad request'"



@pytest.fixture
def get_current_user_data():
    """get current user, return json"""
    data = {}
    r = users.current(s, data)
    r_json = after_processsing(r)
    return r_json

def test_get_current_user_data(get_current_user_data):
    """test json 'status' get current user"""
    assert get_current_user_data["status"] == "ok", "'status' is not 'ok'"

