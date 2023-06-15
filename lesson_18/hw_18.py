import requests
import json
from lession_10 import hw_10_logger as l


def request(function):
    """
    Decorator. Receives request function validate response
    then returns decoded json response
    """
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        if response.status_code == 200:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                l.logger.error('Broken json body received')
        else:
            print(f'>>> Request failed {response.status_code, response.reason} given')

    return wrapper


URL = "https://petstore.swagger.io/v2/pet/"


@request
def get_all_pets(url=URL):
    return requests.get(url=url + "findByStatus", params={"status": "available"})


@request
def create_pet(body, url=URL):
    return requests.post(url=url, json=body)


@request
def get_pet(pet_id, url=URL):
    return requests.get(url=url + pet_id)


@request
def delete_pet(pet_id, url=URL):
    return requests.delete(url=url + pet_id)


def filter_pets():
    """
    Processing response and make list with  pets names
    """
    pets = []

    for dicts in get_all_pets():
        for k, v in dicts.items():
            if k == "name":
                pets.append(v)
    print(pets)


def add_pet():

    body = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "Dog"
            },
            "name": "Patron",
            "photoUrls": [
                "https://google.com"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "Angry"
                }
            ],
            "status": "available"
        }

    result = create_pet(body)

    try:
        if body == result:
            print(f'>>> {body["category"]["name"]} {body["name"]} successfully created with id: {body["id"]}')
        else:
            print(f'>>> Oops, Something went wrong {body["category"]["name"]} {body["name"]} wasn\'t created')
    except TypeError:
        l.logger.error('Empty response given')


def search_pet():
    try:
        user_search = int(input('>>> Enter pet id: '))
        id_list = []
        for dicts in get_all_pets():
            for k, v in dicts.items():
                if k == 'id':
                    id_list.append(v)

        if user_search in id_list:
            print(f'>>> Pet with id: {user_search} exists')
        else:
            print(f'>>> Pet with id: {user_search} wasn\'t found')
    except ValueError:
        l.logger.error('Incorrect ID value entered')


def delete_pet_by_id():
    try:
        user_search = input('>>> Enter pet id: ')
        response_body = delete_pet(user_search)
        if response_body["message"] == user_search:
            print(f'>>> Pet ID {user_search} successfully deleted')
    except TypeError:
        l.logger.error('ID value doesn\'t exist')


filter_pets()
add_pet()
search_pet()
delete_pet_by_id()
