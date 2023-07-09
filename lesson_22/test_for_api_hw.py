from hillel_api import *

# to run tests - pytest less22/test_for_api.py

def test_sigin_positive():

    user_data = {
    "email": "testikpew8@test.com",
    "password": "Qwerty12345",
    "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


# def test_sigin_negative():

#     user_data_negative = {
#     "email": "qam@2022test.com",
#     "password": "Qam2",
#     "remember": False
#     }
#     r = auth.signin(s, user_data_negative)
#     r_json = after_processsing(r)
#     assert r.status_code == 400, "Wrong status code"
#     assert r_json["status"] == "error", "Key 'status' is not error"

# homework 1

def test_get_current_user_positive():
    r = users.current(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no user data"

# homework 2

def test_get_users_profile_positive():
    r = users.profile_get(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no user data"

# homework 3

def test_get_users_settings_positive():
    r = users.settings_get(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no user data"


# homework 4

def test_create_car_positive():
    create_car_ok_data = {
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 23
    }
    r = cars.cars_post(s, create_car_ok_data)
    r_json = after_processsing(r)
    assert r.status_code == 201, "Wrong status code"  # documentation has a bug, it says code 200 is expected
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no car data"


# homework 5

def test_put_users_settings_positive():
    settings_ok_data = {
    "currency": "eur",
    "distanceUnits": "km"
    }
    r = users.settings_put(s, settings_ok_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code" 
    assert r_json["status"] == "ok", "'status' is not ok"
    assert r_json["data"], "Recieved no settings data"

# homework 6

def test_put_users_settings_negative_currency_not_found():
    settings_currency_not_found = {
    "currency": "grn",
    "distanceUnits": "km"
    }
    r = users.settings_put(s, settings_currency_not_found)
    r_json = after_processsing(r)
    assert r.status_code == 404, "Wrong status code"
    assert r_json["message"] == "Currency not found" 

# homework 7

def test_put_users_settings_negative_units_not_found():
    settings_units_not_found = {
    "currency": "eur",
    "distanceUnits": "banana"
    }
    r = users.settings_put(s, settings_units_not_found)
    r_json = after_processsing(r)
    assert r.status_code == 404, "Wrong status code"
    assert r_json["message"] == "Distance units not found" 


# homework 8

def test_get_current_user_negative_not_authenticated():
    do_logout = auth.logout(s)
    r = users.current(s, do_logout)
    r_json = after_processsing(r)
    assert r.status_code == 401, "Wrong status code"
    assert r_json["message"] == "Not authenticated", "'status' is not correct"

# homework 9

def test_get_get_users_profile_negative_not_authenticated():
    do_logout = auth.logout(s)
    r = users.profile_get(s, do_logout)
    r_json = after_processsing(r)
    assert r.status_code == 401, "Wrong status code"
    assert r_json["message"] == "Not authenticated", "'status' is not correct"

# homework 10

def test_get_users_settings_negative_not_authenticated():
    do_logout = auth.logout(s)
    r = users.settings_get(s, do_logout)
    r_json = after_processsing(r)
    assert r.status_code == 401, "Wrong status code"
    assert r_json["message"] == "Not authenticated", "'status' is not correct"


def test_logout():

    r = auth.logout(s)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
