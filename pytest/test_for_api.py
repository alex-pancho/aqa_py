from hillel_api import *
import pytest


# фікстура для передачі сесії у всі тести
@pytest.fixture
def api_session():
    s = requests.session()
    return s


def test_sigin_positive(api_session):
    # This test verifies the successful sign-in functionality using valid user credentials.
    # It calls the auth.signin API with correct credentials and expects a response with a status code of 200 and the status key in the response JSON to be 'ok'.
    user_data = {
        "email": "Ihor.@gmail.com",
        "password": "1q2w3e123123",
        "remember": False,
    }
    r = auth.signin(api_session, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_negative(api_session):
    # This test verifies the sign-in functionality with incorrect user credentials.
    # It calls the auth.signin API with incorrect credentials and expects a response with a status code of 400 and the status key in the response JSON to be 'error'.
    user_data_negative = {
        "email": "TEST123@test.com",
        "password": "123321",
        "remember": False,
    }
    r = auth.signin(api_session, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_logout(api_session):
    # This test verifies the logout functionality.
    # It calls the auth.logout API and expects a response with a status code of 200 and the status key in the response JSON to be 'ok'.
    r = auth.logout(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_brands(api_session):
    # This test verifies the retrieval of car brands.
    # It calls the cars.brands API and expects a response with a status code of 200 and the 'brands' key in the response JSON.
    r = cars.brands(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "brands" in r_json, "Key 'brands' not found in response"


def test_expenses_get(api_session):
    # This test verifies the retrieval of expenses for a specific car.
    # It calls the expenses.expenses_get API with a car ID and expects a response with a status code of 200 and the 'expenses' key in the response JSON.
    car_id = 1  # Assuming you have a car with ID 1 for testing purposes
    r = expenses.expenses_get(api_session, {"id": car_id})
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "expenses" in r_json, "Key 'expenses' not found in response"


def test_profile_get(api_session):
    # This test verifies the retrieval of the user profile.
    # It calls the users.profile_get API and expects a response with a status code of 200 and the 'profile' key in the response JSON.
    r = users.profile_get(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "profile" in r_json, "Key 'profile' not found in response"


def test_profile_put(api_session):
    # This test verifies the update of the user profile.
    # It calls the users.profile_put API with new user data and expects a response with a status code of 200 and the status key in the response JSON to be 'ok'.
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
    }
    r = users.profile_put(api_session, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_expenses_post(api_session):
    # This test verifies the creation of a new expense entry.
    # It calls the expenses.expenses_post API with new expense data and expects a response with a status code of 200 and the status key in the response JSON to be 'ok'.
    expense_data = {
        "car_id": 1,  # Assuming you have a car with ID 1 for testing purposes
        "amount": 50.00,
        "description": "Test expense",
    }
    r = expenses.expenses_post(api_session, expense_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_cars_get(api_session):
    # This test verifies the retrieval of cars.
    # It calls the cars.cars_get API and expects a response with a status code of 200 and the 'cars' key in the response JSON.
    r = cars.cars_get(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "cars" in r_json, "Key 'cars' not found in response"


def test_cars_post(api_session):
    # This test verifies the creation of a new car entry.
    # It calls the cars.cars_post API with new car data and expects a response with a status code of 200 and the status key in the response JSON to be 'ok'.
    car_data = {
        "brand": "Test Brand",
        "model": "Test Model",
        "year": 2023,
    }
    r = cars.cars_post(api_session, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
