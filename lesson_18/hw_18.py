import requests
import json


class Pet:

    URL = "https://petstore.swagger.io/v2/pet/"

    def __init__(self, body):
        self.body = body
        self.id = str(body["id"])

    def create_pet(self):
        """
        Creates a new pet then returns response list status code, reason
        and json response body with pet params
        """
        response = requests.post(url=Pet.URL, json=self.body)
        try:
            response_body = response.json()
            return [response.status_code, response.reason], response_body
        except json.decoder.JSONDecodeError:
            print("Broken json body received")

    def get_pet(self):
        """
        Gets the pet by id then returns response list status code, reason
        and json response body with pet params
        """
        response = requests.get(url=Pet.URL + self.id)
        try:
            response_body = response.json()
            return [response.status_code, response.reason], response_body
        except json.decoder.JSONDecodeError:
            print("Broken json body received")

    def delete_pet(self):
        """
        Deletes the pet by id then returns response list status code, reason
        and json server response body
        """
        response = requests.delete(url=Pet.URL + self.id)
        try:
            response_body = response.json()
            return [response.status_code, response.reason], response_body
        except json.decoder.JSONDecodeError:
            print("Broken json body received")

    @classmethod
    def get_available_pets(cls):
        """
        Gets all pets then returns response list status code, reason
        and json response body with all pets and their params
        """
        response = requests.get(url=cls.URL + "findByStatus", params={"status": "available"})
        try:
            response_body = response.json()
            return [response.status_code, response.reason], response_body
        except json.decoder.JSONDecodeError:
            print("Broken json body received")


dog = Pet({
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
})

print(Pet.get_available_pets())
print(dog.create_pet())
print(dog.get_pet())
print(dog.delete_pet())
