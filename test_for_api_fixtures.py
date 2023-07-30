import pytest
from hillel_api import *
from conftest import *

# pytest less23/test_for_api_fixtures.py


def test_reset_password(registered_user):
    reset_data = {
        "email": "notmail@test.com"
    }
    r = auth.resetpassword(s, reset_data)

def test_get_users_profile_positive(logged_user):
    r = users.profile_get(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no user data"

def test_get_cars(logged_user, create_car):

    r = cars.cars_get(s)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not 'ok'"
    assert len(r_json["data"]) == 1, "Wrong amount of cars received"

def test_get_instructions_positive(instructions_data):
    assert len(instructions_data) > 0


def test_get_user_settings(logged_user):
    r = users.settings_get(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no user data"