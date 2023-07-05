from hillel_api import *
import pytest


@pytest.fixture()
def registered_user():
    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    r = auth.signup(s, register_data)
    yield r

    # delete user
    users.users(s)


@pytest.fixture()
def logged_user():
    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    auth.signup(s, register_data)

    # login user
    login_data = {
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "remember": True
    }

    yield auth.signin(s, login_data)

    # delete user
    users.users(s)


def test_signup_positive():
    """Register a new user"""

    user_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii2@test.com",
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


def test_signup_negative(registered_user):
    """Try Register existing user """

    user_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
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
    assert r_json["message"] == 'User already exists', 'Incorrect message received'


def test_signin_positive(registered_user):
    """Login existing user"""

    user_data = {
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_signin_negative(registered_user):
    """Login incorrect password"""

    user_data_negative = {
        "email": "apepsii@test.com",
        "password": "testam2608venv#",
        "remember": False
    }
    r = auth.signin(s, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == 'Wrong email or password', 'Incorrect message received'


def test_logout_positive(logged_user):
    """Logout user"""

    r = auth.logout(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_reset_password_positive(logged_user):
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


def test_reset_password_negative(logged_user):
    """Reset pass old a new passwords don't match"""

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


def test_reset_password_negative2(logged_user):
    """Reset pass new passwords don't match"""

    user_data = {
        "oldPassword": "Qam2608venv#",
        "password": "123Abc+-=",
        "repeatPassword": "123Abc+-"
    }

    r = users.resetpassword(s, user_data)
    r_json = after_processsing(r)

    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'ok'"
    assert r_json["message"] == "Passwords do not match", "Incorrect error message"


def test_change_email_positive(logged_user):
    """Change users email"""

    user_data = {
        "email": "testanatolii@gmail.com",
        "password": "Qam2608venv#"
    }

    r = users.email(s, user_data)
    r_json = after_processsing(r)

    assert r.status_code == 200, f"Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_current_positive(logged_user):
    """Get user info"""

    r = users.current(s)
    r_json = after_processsing(r)

    # Get test user json
    r_users_json = after_processsing(logged_user)

    assert r.status_code == 200, "Wrong status code"
    assert r_json == r_users_json, "Current user's data is not correct"


def test_current_negative():
    """Get user info when not logged in"""

    r = users.current(s)
    r_json = after_processsing(r)

    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Not authenticated", "Incorrect error message"


def test_profile_put_positive(logged_user):
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


def test_settings_get_positive(logged_user):
    """Get user settings"""

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


def test_delete_user_positive(logged_user):
    """Delete user"""
    r = users.users(s)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"
