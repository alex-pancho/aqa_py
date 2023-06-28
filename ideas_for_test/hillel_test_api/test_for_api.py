import pytest
import requests
import datetime
import inspect
from ideas_for_test.hillel_test_api.tes_hillel_loger import logger

from ideas_for_test.hillel_test_api.enums.global_enums import GlobalErrorMessages as gl
from ideas_for_test.hillel_test_api.enums.global_enums import GlobalErrorDict as gled
from ideas_for_test.hillel_test_api.enums.global_enums import *
from ideas_for_test.hillel_test_api.hillel_api import *
from ideas_for_test.hillel_test_api.hillel_api import after_processsing, auth
from http.client import HTTPConnection


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


# @pytest.mark.skip
@pytest.mark.parametrize("debug_level", [1])
# @pytest.mark.positive
def test_instructions_initial_info_positive_flow(debug_level):
    '''verify response with no query params'''
    HTTPConnection.debuglevel = debug_level
    instr = instructions()  # Створення екземпляру класу instructions
    r = instr.instructions_initial_info(s, request_body={})
    r_json = after_processsing(r)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", gl.NOT_STATUS_OK.value
    assert r_json["currentPage"] == 1, "Initial page is not 1"
    assert isinstance(r_json["currentPage"], int), gl.NOT_STR_INSTANSE.value
    assert isinstance(r_json["data"], list)
    for item in r_json["data"]:
        assert isinstance(item["id"], int), gl.NOT_INT_INSTANSE.value
        assert isinstance(item["filename"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["description"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["carBrandId"], int), gl.NOT_INT_INSTANSE.value
        assert isinstance(item["carModelId"], int), gl.NOT_INT_INSTANSE.value

    assert isinstance(r_json["totalItems"], int), gl.NOT_LIST_INSTANSE.value


@pytest.mark.parametrize("debug_level", [1])
def test_instructions_initial_info_incorrect_path(debug_level):
    '''verify error due to incorrect path in uri'''
    HTTPConnection.debuglevel = debug_level
    incorrect_endpoint = "/instruction"  # no <s> in the end
    response = s.get(f"{base_api_url}/{incorrect_endpoint}")
    json_response = response.json()

    assert response.status_code == 404, gl.RAISE_404_ERROR.value
    assert json_response == gled.error_404_found.value
    assert isinstance(datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z'),
                      datetime.datetime)
    assert response.headers['Server'] == H_SERVER
    assert response.headers['Content-Type'] == H_CONTENT_TYPE
    assert 'Content-Length' in response.headers, gl.NO_CONTENT_LENGHTH.value
    assert response.headers['Connection'] == H_CONNECTION
    assert response.headers['X-Powered-By'] == H_X_POWERED_BY
    assert response.headers['Vary'] == H_VARY
    assert response.headers['Access-Control-Allow-Credentials'] == H_ACC_CONTROL_ALLOW_CRED
    assert 'Content-Length' in response.headers, gl.NO_CONTENT_LENGHTH.value
    assert 'Etag' in response.headers, gl.NO_ETAG


@pytest.mark.parametrize("debug_level", [1])
# @pytest.mark.positive
def test_instructions_with_default_values_query_params(debug_level):
    '''verify response with default params'''
    HTTPConnection.debuglevel = debug_level
    r = instructions.instructions(s, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    assert isinstance(r_json["currentPage"], int), gl.NOT_STR_INSTANSE.value
    assert isinstance(r_json["data"], list)
    for item in r_json["data"]:
        assert isinstance(item["id"], int), gl.NOT_INT_INSTANSE.value
        assert isinstance(item["filename"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["description"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["carBrandId"], int), gl.NOT_INT_INSTANSE.value
        assert isinstance(item["carModelId"], int), gl.NOT_INT_INSTANSE.value
    assert isinstance(r_json["totalItems"], int), gl.NOT_LIST_INSTANSE.value


@pytest.mark.parametrize("page, car_brand_id, car_model_id", [
    (1, 1, 1),
])
def test_instructions_with_min_values_query_params(page, car_brand_id, car_model_id):
    '''quiq verifing positive response with min params'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["currentPage"] == query_params["page"], f"Response page is not matched to {query_params['page']}"


@pytest.mark.parametrize("page, car_brand_id, car_model_id", [
    (1, 1, 1),
])
def test_instructions_min_values_response_attribues(page, car_brand_id, car_model_id):
    '''verify types and min values in response attribures'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json["currentPage"] == query_params["page"], f"Response page is not matched to {query_params['page']}"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    assert isinstance(r_json["currentPage"], int), gl.NOT_STR_INSTANSE.value
    assert r_json["currentPage"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
    assert isinstance(r_json["data"], list)
    for item in r_json["data"]:
        assert isinstance(item["id"], int), gl.NOT_INT_INSTANSE.value
        assert item["id"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
        assert isinstance(item["filename"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["description"], str), gl.NOT_STR_INSTANSE.value
        assert isinstance(item["carBrandId"], int), gl.NOT_INT_INSTANSE.value
        assert item["carBrandId"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
        assert isinstance(item["carModelId"], int), gl.NOT_INT_INSTANSE.value
        assert item["carModelId"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
    assert isinstance(r_json["totalItems"], int), gl.NOT_LIST_INSTANSE.value


@pytest.mark.parametrize("page, car_brand_id, car_model_id, doubtful", [
    (0, 0, 0, True),  # Підозріла поведінка АРІ або системи
])
def test_instructions_with_zero_in_values_query_params(page, car_brand_id, car_model_id, doubtful):
    '''quiq verifing positive response with zero params'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    assert r_json[
               "currentPage"] >= MIN_ATTR_VALUE_INSTRUCTION, f"Response page is not matched to {query_params['page']}"
    assert r_json["totalItems"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value

    if doubtful:
        logger.warning(f"Test <{inspect.currentframe().f_code.co_name}> is marked as doubtful")


@pytest.mark.parametrize("doubtful", [
    (True),  # Підозріла поведінка АРІ або системи
])
def test_instructions_with_no_query_params(doubtful):
    '''quiq verifing positive response with zero params'''
    query_params = {}
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    assert r_json["currentPage"] >= MIN_ATTR_VALUE_INSTRUCTION
    assert r_json["totalItems"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value

    if doubtful:
        logger.warning(f"Test <{inspect.currentframe().f_code.co_name}> is marked as doubtful")


@pytest.mark.parametrize("page, car_brand_id, car_model_id, doubtful", [
    (1, None, None, True),  # Підозріла поведінка АРІ або системи
    (2, None, None, True),
    (10, None, None, True),
    (20, None, None, True),
    pytest.param(100, None, None, True, marks=pytest.mark.xfail(reason="Expected failure")),
    ], ids=["1", "2", "10", "20", "100 (Expected failure)"]) #expected test failure


def test_instructions_with_page_query_param(page, car_brand_id, car_model_id, doubtful):
    '''verify positive response with page query param only'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    assert r_json["currentPage"] >= MIN_ATTR_VALUE_INSTRUCTION
    assert r_json["currentPage"] == query_params['page']
    assert r_json["totalItems"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value

    if doubtful:
        logger.warning(f"Test <{inspect.currentframe().f_code.co_name}> is marked as doubtful")

@pytest.mark.parametrize("page, car_brand_id, car_model_id, doubtful", [
    (None, 1, None, True),  # Підозріла поведінка АРІ або системи
    (None, 2, None, True),
    (None, 3, None, True),
    (None, 4, None, True),
    pytest.param(None, 1, None, True, marks=pytest.mark.xfail(reason="Expected failure")),
    ], ids=["1", "2", "3", "4", "100 (Expected failure)"])  # expected test failure

def test_instructions_with_car_brand_id_query_param(page, car_brand_id, car_model_id, doubtful):
    '''verify positive response with car_brand_id query param only'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    item_present = False  # Флаг, що відстежує наявність item у data

    for item in r_json["data"]:
        item_present = True  # Позначаємо, що item присутній у data
        assert isinstance(item["carBrandId"], int), gl.NOT_INT_INSTANSE.value
        assert item["carBrandId"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
        assert item["carBrandId"] >= query_params['carBrandId'], gl.NOT_MATCHED_TO_EXPECTED_VALUE.value

    if not item_present:
        raise ValueError(gl.VALUE_IS_NONE.value)

    if doubtful:
        logger.warning(f"Test <{inspect.currentframe().f_code.co_name}> is marked as doubtful")


@pytest.mark.parametrize("page, car_brand_id, car_model_id, doubtful", [
    (None, None, 1, True),  # Підозріла поведінка АРІ або системи
    (None, None, 2, True),
    (None, None, 3, True),
    (None, None, 4, True),
    pytest.param(None, 1, None, True, marks=pytest.mark.xfail(reason="Expected failure")),
    ], ids=["1", "2", "3", "4", "100 (Expected failure)"])  # expected test failure

def test_instructions_with_car_model_id_query_param(page, car_brand_id, car_model_id, doubtful):
    '''verify positive response with car_model_id query param only'''
    query_params = {"page": page,
                    "carBrandId": car_brand_id,
                    "carModelId": car_model_id
                    }
    r = instructions.instructions_refactor(s, query_params=query_params, request_body={})
    r_json = after_processsing(r)
    print(r_json)
    assert r.status_code == 200, "Wrong status code"
    assert r_json.get("status") == "ok", gl.NOT_STATUS_OK.value
    item_present = False  # відстежуємо наявність item у data

    for item in r_json["data"]:
        item_present = True  # Позначаємо, що item присутній у data
        assert isinstance(item["carModelId"], int), gl.NOT_INT_INSTANSE.value
        assert item["carModelId"] >= MIN_ATTR_VALUE_INSTRUCTION, gl.NOT_MATCHED_TO_MIN_VALUE.value
        assert item["carModelId"] >= query_params['carModelId'], gl.NOT_MATCHED_TO_EXPECTED_VALUE.value

    if not item_present:
        raise ValueError(gl.VALUE_IS_NONE.value)
    logger.info(f"Item in test <{inspect.currentframe().f_code.co_name}> {gl.NOT_INT_INSTANSE.value}")

    if doubtful:
        logger.warning(f"Test <{inspect.currentframe().f_code.co_name}> is marked as doubtful")