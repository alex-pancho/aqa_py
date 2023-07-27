import requests
import pytest
from hillel_api import auth, cars, expenses, users, after_processsing


# Фікстура для ініціалізації API сесії:
@pytest.fixture
def api_session():
    s = requests.session()
    return s


# Фікстура для створення тестового користувача:
@pytest.fixture
def test_user_data():
    user_data = {
        "email": "testuser@example.com",
        "password": "TestPassword123",
        "remember": False,
    }
    return user_data


# Фікстура для створення тестового автомобіля:
@pytest.fixture
def test_car_data():
    car_data = {
        "brand": "Test Brand",
        "model": "Test Model",
        "year": 2023,
    }
    return car_data


# Фікстура для авторизації користувача перед кожним тестом:
@pytest.fixture(autouse=True)
def authenticate_user(api_session, test_user_data):
    r = auth.signin(api_session, test_user_data)
    assert r.status_code == 200, "Failed to sign in test user"
    yield
    auth.logout(api_session)


# Фікстура для створення тестового витрати:
@pytest.fixture
def test_expense_data():
    expense_data = {
        "car_id": 1,  # Assuming you have a car with ID 1 for testing purposes
        "amount": 50.00,
        "description": "Test expense",
    }
    return expense_data


def test_sigin_positive(api_session, test_user_data):
    user_data = test_user_data
    r = auth.signin(api_session, user_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_negative(api_session):
    user_data_negative = {
        "email": "nonexistentuser@example.com",
        "password": "InvalidPassword123",
        "remember": False,
    }
    r = auth.signin(api_session, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_create_car(api_session, test_car_data):
    car_data = test_car_data
    r = cars.cars_post(api_session, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_create_expense(api_session, test_expense_data):
    expense_data = test_expense_data
    r = expenses.expenses_post(api_session, expense_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_get_user_profile(api_session):
    r = users.profile_get(api_session)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert "profile" in r_json, "Key 'profile' not found in response"
