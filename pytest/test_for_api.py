from hillel_api import *
import pytest


# фікстура для передачі сесії у всі тести
@pytest.fixture
def api_session():
    s = requests.session()
    return s


def test_sigin_positive(api_session):
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
    r = auth.logout(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_brands(api_session):
    r = cars.brands(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "brands" in r_json, "Key 'brands' not found in response"


def test_expenses_get(api_session):
    car_id = 1  # Assuming you have a car with ID 1 for testing purposes
    r = expenses.expenses_get(api_session, {"id": car_id})
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "expenses" in r_json, "Key 'expenses' not found in response"


def test_profile_get(api_session):
    r = users.profile_get(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "profile" in r_json, "Key 'profile' not found in response"


def test_profile_put(api_session):
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
    }
    r = users.profile_put(api_session, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_expenses_post(api_session):
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
    r = cars.cars_get(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "cars" in r_json, "Key 'cars' not found in response"


def test_cars_post(api_session):
    car_data = {
        "brand": "Test Brand",
        "model": "Test Model",
        "year": 2023,
    }
    r = cars.cars_post(api_session, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
