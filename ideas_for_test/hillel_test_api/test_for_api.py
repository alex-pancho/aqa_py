from hillel_api import *
import pytest


@pytest.fixture()
def new_user():

    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsi@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
        }
    auth.signup(s, register_data)

    # login user
    login_data = {
        "email": "apepsi@test.com",
        "password": "Qam2608venv#",
        "remember": True
        }
    r = auth.signin(s, login_data)
    yield r

    # delete test user
    users.users(s)


def test_signup_positive():
    """Register a new user"""

    user_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsi@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    # Create test user
    r = auth.signup(s, user_data)
    r_json = after_processsing(r)

    # Delete test user
    users.users(s)

    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == 'ok', "Key 'status' is not 'ok'"


def test_signup_negative():
    """Try Register existing user """

    user_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "pepsi@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    # Create a new user
    auth.signup(s, user_data)

    # Register a new user with same values
    r = auth.signup(s, user_data)
    r_json = after_processsing(r)

    # Delete test user
    users.users(s)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == 'error', "Key 'status' is not 'error'"
    assert r_json["message"] == 'User already exists'


def test_sigin_positive():
    """Login existing user"""

    user_data = {
        "email": "qam2608@2023test.com",
        "password": "Qam2608venv#",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_sigin_negative():
    """Login incorrect password"""

    user_data_negative = {
        "email": "qam@2023test.com",
        "password": "Qam2",
        "remember": False
    }
    r = auth.signin(s, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"


def test_logout_positive():
    """Logout user"""

    r = auth.logout(s)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_reset_password_positive(new_user):
    """Reset pass"""

    user_data = {
        "oldPassword": "Qam2608venv#",
        "password": "123Abc+-=",
        "repeatPassword": "123Abc+-="
    }

    r = users.resetpassword(s, user_data)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_reset_password_negative(new_user):
    """Reset pass passwords doesn't match"""

    user_data = {
        "oldPassword": "Qam2608venv",
        "password": "123Abc+-=",
        "repeatPassword": "123Abc+-="
    }

    r = users.resetpassword(s, user_data)
    r_json = after_processsing(r)

    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'ok'"
    assert r_json["message"] == "Wrong password", "Incorrect error message"


def test_change_email_positive(new_user):
    """Change users email"""

    user_data = {
        "email": "test1323123@test.com",
        "password": "Qam2608venv#"
    }

    r = users.email(s, user_data)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_current_positive(new_user):
    """Get user info"""

    r = users.current(s)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_current_negative():
    """Get user info when not logged in"""

    r = users.current(s)
    r_json = after_processsing(r)

    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Not authenticated", "Incorrect error message"


def test_profile_put(new_user):
    """Update user data"""
    new_user_data = {

        "photo": "user-1621352948859.jpg",
        "name": "John",
        "lastName": "Dou",
        "dateBirth": "2021-03-17T15:21:05.000Z",
        "country": "Ukraine"
    }

    r = users.profile_put(s, new_user_data)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_settings_get(new_user):
    "Get user settings"

    r = users.settings_get(s)
    r_json = after_processsing(r)
    expected_json = {
                      "status": "ok",
                      "data": {
                          "currency": "usd",
                          "distanceUnits": "km"
                        }
    }

    assert r.status_code == 200, "Wrong status code"
    assert r_json == expected_json, "Wrong json response received"


def test_delete_user(new_user):
    """Delete user"""
    r = users.users(s)
    r_json = after_processsing(r)

    assert r.status_code == 200
    assert r_json["status"] == "ok"







