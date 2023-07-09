from hillel_api import *
import pytest


    
def test_sigin_positive():

    user_data = {
    "email": "qam2608@2022test.com",
    "password": "Qam2608venv",
    "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_negative():

    user_data_negative = {
    "email": "qam@2022test.com",
    "password": "Qam2",
    "remember": False
    }
    r = auth.signin(s, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_logout():

    r = auth.logout(s)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

"""Мої тести"""


def test_brands():
    """Перевіряємо відповідь з параметрами по замовченню""" 
    r = cars.brands(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ok", "Status is not ok"


def test_brands_id():
    """Перевіряємо відповідь з параметром id """
    car_data={
        "id": 2
    }

    r = cars.brands_id (s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ok", "Status is not ok"


def test_brands_id_negative():
    """id str замість int"""
    car_data = {
        "id": "car"
    }

    r = cars.brands_id(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 404, "Status code is not correct"
    assert r_json["status"] == "error", "Status is not ok"


def test_models():
    """Перевіряємо відповідь на запит моделі авто по id"""
    car_data={
        "id": 2
    }

    r = cars.models (s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ok", "Status is not ok"


def test_models_negative():
    """Перевіряємо відповідь на запит моделі авто по id, якщо id str"""
    car_data={
        "id": "model"
    }

    r = cars.models (s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 404, "Status code is not correct"
    assert r_json["status"] == "error", "Status is not ok"

def test_models_id():
    """Перевіряємо відповідь при запиті по id, чи відповідає тому що запитували"""
    car_data={
        "id": "2"
    }

    r = cars.models_id(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ok", "Status is not ok"
    assert r_json["data"]["id"] == 2, "Initial page id value is incorrect"


def test_cars_post():
    '''Перевірка створення нового авто'''
      
    user_data={
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    auth_response = auth.signin (s, user_data)
    assert auth_response.status_code == 200, "Authorization failed"
    car_data={
        "carBrandId": 5,
        "carModelId": 5,
        "mileage": 4343434
    }
    r = cars.cars_post(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ok", "Status is not ok"
    assert r_json["message"] == "Car is added"


def test_cars_post_negative():
    '''Негативна перевірка відповіді з параметрами по замовченню і не авторизованим користувачем'''
    car_data={
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 1
}
    r = cars.cars_post(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not ok"
    assert r_json["message"] == "Not authenticated"


def test_car_id_put():
    '''Перевірка відповіді з параметрами по замовченню , користувач авторизован'''

    user_data={
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    auth_response = auth.signin(s, user_data)
    assert auth_response.status_code == 200, "Authorization failed"

    car_data = {
        "reportedAt": "2020-01-10",
        "mileage": 2222,
        "liters": 22,
        "totalCost": 123,
        "forceMileage": False
    }
    r = cars.cars_id_put(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Status code is not correct"
    assert r_json["status"] == "ок", "Status is not ok"
    assert r_json["message"] == "Information is updated"

def cars_id_delete_neg():
    '''Перевірка на delete'''

    user_data={
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }

    auth_response=auth.signin (s, user_data)
    assert auth_response.status_code == 200, "Authorization failed"

    car_data={
        "id": 5
    }

    r = cars.cars_id_delete(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json["message"] == "Car successfully deleted"