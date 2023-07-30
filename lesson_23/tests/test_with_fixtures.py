import pytest
import requests
import datetime
import random
import string


base_api_url = "https://qauto.forstudy.space/api"
status_codes = {
    "success": 200,
    "created": 201,
    "bad_request": 400,
    "User not logged in": 401
}

status_msg = [
    "ok",
    "Bad request error",
    "Successfully received the data",
    "User is not logged in",
    "error",
    "Incorrect data was recieved",
    "Creates user, user profile and user settings, and authenticates created user."

]

user_data = {
    "userId": 39456,
    "currency": "usd",
    "distanceUnits": "km",
    "photoFilename": "default-user.png"
}

user_profile = {

    "userId": 39456,
    "photoFilename": "default-user.png",
    "name": "John",
    "lastName": "Doulksdf"
}

# HEADERS ATTRIBUTES:
H_SERVER = "nginx/1.18.0 (Ubuntu)"
H_CONTENT_TYPE = "application/json; charset=utf-8"
H_CONNECTION = "keep-alive"
H_X_POWERED_BY = "Express"
H_VARY = "Origin"
H_ACC_CONTROL_ALLOW_CRED = "true"


@pytest.fixture(scope='session', autouse=False)
def signin():
    '''Get signin to API'''
    s = requests.session()
    user_data = {
        "email": "qam2608@2022dtest.com",
        "password": "Qwerty12345",
        "remember": False
    }
    endpoint = "/auth/signin"
    try:
        response = s.post(base_api_url + endpoint, json=user_data)
        # print("Headers in signin:n/", response.headers)
        response_json = response.json()
        # print("resp signin:", response_json)

        response.raise_for_status()  # Перевірка на наявність помилки у відповіді
    except (ConnectionError, requests.exceptions.HTTPError) as e:
        print("No connection or error in response:", str(e))
    yield s, response_json  # ретьорнимо об'єкт сесії з кукі і обєкт респонс в json-i


def pytest_generate_tests(metafunc):
    '''Generate user-data'''
    if 'user_data' in metafunc.fixturenames:
        attr2 = ''.join(random.choices(string.ascii_letters, k=2)) #generate 2 ascii characters
        attr20 = ''.join(random.choices(string.ascii_letters, k=20)) #generate 20 ascii characters
        attr15 = ''.join(random.choices(string.ascii_letters, k=15)) #generate 15 ascii characters

        metafunc.parametrize('user_data', [
            {
                "name": f"{attr2}", #test minLength: 2
                "lastName": f"{attr2}",#test minLength: 2
                "email": f"{attr2}25kosko@kotest.com",
                "password": "Qwerty12311",
                "repeatPassword": "Qwerty12311"
            },
            {
                "name": f"{attr20}", #test maxLength: 20
                "lastName": f"{attr20}", #test maxLength: 20
                "email": f"{attr2}26_kosko@kotest.com",
                "password": "Qwwety12349",
                "repeatPassword": "Qwwety12349"
            },
            {
                "name": f"{attr2}",  # test minLength: 2
                "lastName": f"{attr2}",  # test minLength: 2
                "email": f"{attr2}@k.com",# test minLength: 8
                "password": "Qwerty12311",
                "repeatPassword": "Qwerty12311"
            },
            {
                "name": f"{attr20}",  # test maxLength: 20
                "lastName": f"{attr20}",  # test maxLength: 20
                "email": f"{attr15}@k.om",
                "password": "Qwwety12349",
                "repeatPassword": "Qwwety12349"
            }
        ])


@pytest.fixture(scope='session')
def signup():
    '''signup new user'''
    s = requests.session()

    def _signup(user_data):
        endpoint = "/auth/signup"
        try:
            response = s.post(base_api_url + endpoint, json=user_data)
            response.raise_for_status()  # Перевірка на наявність помилки у відповіді

        except (ConnectionError, requests.exceptions.HTTPError) as k:
            print("No connection or error in response:", str(k))
        return response

    return _signup
    # TODO: "розробити видалення створеного користувача після завершення тестів"через s.delete(base_api_url + f"/users")



def test_signup(signup, user_data):
    '''verification positive tc for signup'''
    response = signup(user_data)
    assert response.status_code == status_codes[
        "created"], f"Incorrect status code. Got {response.status_code} but expected {status_codes['created']}"


@pytest.fixture()
def after_processsing():
    '''Get response in json format'''
    def process_response(response):
        try:
            return response.json()
        except Exception as h:
            print("Incorrect request or response data", str(h))
            return {}

    return process_response


@pytest.fixture()
def validate_response_headers(request):
    def validate_headers(response, endpoint, http_method):
        try:
            assert isinstance(datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z'),
                              datetime.datetime)
            assert response.headers['Server'] == H_SERVER
            assert response.headers['Content-Type'] == H_CONTENT_TYPE
            assert 'Content-Length' in response.headers
            assert response.headers['Connection'] == H_CONNECTION
            assert response.headers['X-Powered-By'] == H_X_POWERED_BY
            assert response.headers['Vary'] == H_VARY
            assert response.headers['Access-Control-Allow-Credentials'] == H_ACC_CONTROL_ALLOW_CRED
            assert 'Content-Length' in response.headers
            assert 'Etag' in response.headers
        except AssertionError as e:
            # обробка невдалих перевірок
            print("Assertion error:", str(e))
            # виклик pytest.fail()
            pytest.fail("One or more assertions failed")

    return validate_headers


def test_users_current(signin, after_processsing, validate_response_headers):
    '''Verify uccessfully received the data in current endpoint'''
    s_cookies = signin[0]
    s_resp_json = signin[1]
    endpoint = "/users/current"
    response = s_cookies.get(f"{base_api_url}{endpoint}")
    json_response = after_processsing(response)
    assert response.status_code == status_codes[
        "success"], f"Incorrect status code. Got {response.status_code} but expected {status_codes['success']}"
    assert json_response["status"] == status_msg[
        0], f"Incorrect status message. Got {response.status_code} but expected {status_msg[0]}"
    assert s_resp_json['data'] == user_data, f"{status_msg[5]}"
    validate_response_headers(response, endpoint, 'GET')


def test_get_error_current_endpoint_without_coocies(after_processsing, validate_response_headers):
    '''Vefiry error 401 due to lack of coocies'''
    endpoint = "/users/current"
    response = requests.get(f"{base_api_url}{endpoint}")
    json_response = after_processsing(response)
    assert response.status_code == status_codes[
        "User not logged in"], f"Incorrect status code. Got <{response.status_code}> but expected <{status_codes['User not logged in']}>"
    validate_response_headers(response, endpoint, 'GET')


def test_get_user_profile_data(signin, after_processsing, validate_response_headers):
    s_cookies = signin[0]
    endpoint = "/users/profile"
    response = s_cookies.get(f"{base_api_url}{endpoint}")
    json_response = after_processsing(response)
    assert response.status_code == status_codes[
        "success"], f"Incorrect status code. Got {response.status_code} but expected {status_codes['success']}"
    assert json_response["status"] == status_msg[
        0], f"Incorrect status message. Got {response.status_code} but expected {status_msg[0]}"
    assert json_response['data']['userId'] == user_profile['userId']
    assert json_response['data']['photoFilename'] == user_profile['photoFilename']
    assert json_response['data']['name'] == user_profile['name']
    assert json_response['data']['lastName'] == user_profile['lastName']
    validate_response_headers(response, endpoint, 'GET')


def test_logout(signin, after_processsing, validate_response_headers):
    '''Check successful logout after signin'''
    s_cookies = signin[0]
    endpoint = "/auth/logout"
    response = s_cookies.get(f"{base_api_url}{endpoint}")
    json_response = after_processsing(response)
    assert response.status_code == status_codes[
        "success"], f"Incorrect status code. Got {response.status_code} but expected {status_codes['success']}"
    assert json_response["status"] == status_msg[
        0], f"Incorrect status message. Got {response.status_code} but expected {status_msg[0]}"
    validate_response_headers(response, endpoint, 'GET')
