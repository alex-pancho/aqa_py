import pytest
from hillel_api import *


# create new user
@pytest.fixture()
def registered_user():
    register_data = {
        "name": "notuser",
        "lastName": "pewpew",
        "email": "notmail@test.com",
        "password": "Notpassword1!",
        "repeatPassword": "Notpassword1!"
    }
    r = auth.signup(s, register_data)
    yield r
    # Delete user
    users.users(s)

# create user, log in
@pytest.fixture()
def logged_user():
    register_data = {
        "name": "notuser",
        "lastName": "pewpew",
        "email": "notmail@test.com",
        "password": "Notpassword1!",
        "repeatPassword": "Notpassword1!"
    }
    auth.signup(s, register_data)

    login_data = {
        "email": "notmail@test.com",
        "password": "Notpassword1",
        "remember": True
    }

    r = auth.signin(s, login_data)
    yield r

    # Delete user
    users.users(s)


# create new car
@pytest.fixture()
def create_car():
    create_car_ok_data = {
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 23
    }
    r = cars.cars_post(s, create_car_ok_data)
    r_json = after_processsing(r)

    car_id = r_json["data"]["id"]
    yield car_id
    cars.cars_id_delete(s, car_id)

# get instructions
@pytest.fixture()
def instructions_data(registered_user, create_car):
    use_this = {
        "carBrandId": 1,
        "carModelId": 1,
        "page": 1
    }
    r = instructions.instructions(s, use_this)
    r_json = after_processsing(r)
    yield r_json

