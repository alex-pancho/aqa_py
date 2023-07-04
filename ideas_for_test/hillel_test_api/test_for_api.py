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


def test_car_brends():
    '''Проверка ответа с параметрами по умолчанию'''

    r = cars.brands(s)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    data=r_json["data"]
    assert isinstance (data, list), "Expected 'list' to be an instance of 'list'"


def test_car_brands_id():
    '''Проверка положительного ответа с минимальными параметрами'''

    car_data = {
        "id": 2
    }

    r = cars.brands_id(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", "Key 'status' is not ok"

    data = r_json.get("data")
    assert isinstance(data, dict), "Expected 'data' to be an instance of 'dict'"
    assert isinstance(data.get("title"), str), "Expected 'title' to be an instance of 'str'"
    assert isinstance(data.get("logoFilename"), str), "Expected 'logoFilename' to be an instance of 'str'"


def test_car_brands_id_neg():
    '''ативная проверка с буквеным значением в id'''
    car_data = {
        "id": "dd"
    }

    r=cars.brands_id (s, car_data)
    r_json=after_processsing (r)
    data=r_json.get ("data")
    assert r.status_code == 404, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"
    assert isinstance ("status", str), "Expected 'message' to be an instance of 'str'"
    assert isinstance ("message", str), "Expected 'status' to be an instance of 'str'"

def test_car_brands_models_id():
    '''Проверка типов и значений в атрибутах ответа'''
    car_data = {
        "id": "3"
    }

    r = cars.models_id(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["data"]["id"] == 3, "Initial page id value is incorrect"

    data = r_json["data"]
    assert isinstance(data, dict), "Expected 'data' to be an instance of 'dict'"
    assert isinstance(data.get("id"), int), "Expected 'id' to be an instance of 'int'"
    assert isinstance(data.get("carBrandId"), int), "Expected 'carBrandId' to be an instance of 'int'"
    assert isinstance(data.get("title"), str), "Expected 'title' to be an instance of 'str'"


def test_car_brands_models_id_neg():
    '''Негативная проверка с пустым значением car_data'''
    car_data={
    "carBrandId": "",
    "carModelId": "",
    "mileage": ""
}

    r = cars.models_id(s, car_data)
    r_json=after_processsing (r)
    assert r.status_code == 404, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"
    assert isinstance ("status", str), "Expected 'status' to be an instance of 'str'"
    assert isinstance ("message", str), "Expected 'message' to be an instance of 'str'"


def test_car_brands_cars_post():
    '''Проверка ответа с параметрами по умолчанию и авторизированым пользователем'''
      #Тест написан правильно но тк в апи ошибка то будет статус 400
    user_data={
    "email": "qam2608@2022test.com",
    "password": "Qam2608venv",
    "remember": False
    }
    auth_response=auth.signin (s, user_data)
    assert auth_response.status_code == 200, "Authorization failed"
    car_data={
    "carBrandId": 5,
    "carModelId": 5,
    "mileage": 4343434
}
    r = cars.cars_post(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json["message"] == "Car is added"



def test_car_brands_cars_post_neg():
    '''Негативная проверка ответа с параметрами по умолчанию и не авторизированым пользователем'''
    car_data={
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 1
}
    r = cars.cars_post(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"
    assert r_json["message"] == "Not authenticated"



def test_car_brands_cars_id_put():
    '''Проверка ответа с параметрами по умолчанию и авторизированым пользователем'''
    user_data={
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    auth_response = auth.signin(s, user_data)
    assert auth_response.status_code == 200, "Authorization failed"

    car_data = {
        "reportedAt": "2021-05-17",
        "mileage": 111,
        "liters": 11,
        "totalCost": 11,
        "forceMileage": False
    }
    r = cars.cars_id_put(s, car_data)
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ок", "Key 'status' is not ok"
    assert r_json["message"] == "Information is updated"


def cars_id_delete_neg():
    '''Проверка ответа с параметрами по умолчанию и авторизированым пользователем'''
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
    data=r_json["data"]
    assert isinstance (data, dict), "Expected 'data' to be an instance of 'dict'"
    assert isinstance (data.get("id"), int), "Expected 'id' to be an instance of 'int'"
    assert isinstance (data.get("carBrandId"), str), "Expected 'title' to be an instance of 'str'"
    assert isinstance (data.get("title"), str), "Expected 'logoFilename' to be an instance of 'str'"








