import pytest
import requests

# from ideas_for_test.hillel_test_api.hillel_api import after_processsing, s, auth, base_api_url

base_api_url = "https://qauto.forstudy.space/api"


@pytest.fixture(scope='session', autouse=False)
def signin():
    s = requests.session()
    user_data = {
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    endpoint = "/auth/signin"
    try:
        response = s.post(base_api_url + endpoint, json=user_data)
        print("Headers in signin:n/", response.headers)
        response.raise_for_status()  # Перевірка на наявність помилки у відповіді
    except (ConnectionError, requests.exceptions.HTTPError) as e:
        print("No connection or error in response:", str(e))
    yield s  # ретьорнимо об'єкт сесії з кукі


@pytest.fixture()
def after_processsing():
    def process_response(response):
        try:
            return response.json()
        except Exception as h:
            print("Incorrect request or response data", str(h))
            return {}
    return process_response

