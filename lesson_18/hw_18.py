import requests


class Pet:

    URL = "https://petstore.swagger.io/v2/pet/"

    def __init__(self, body):
        self.body = body
        self.id = str(body["id"])

    def create_pet(self) -> tuple:
        response = requests.post(url=Pet.URL, json=self.body)
        return [response.status_code, response.reason], response.content

    def get_pet(self) -> tuple:
        response = requests.get(url=Pet.URL + self.id)
        return [response.status_code, response.reason], response.content

    def delete_pet(self) -> tuple:
        response = requests.delete(url=Pet.URL + self.id)
        return [response.status_code, response.reason], response.content

    @classmethod
    def get_available_pets(cls) -> tuple:
        response = requests.get(url=cls.URL + "findByStatus", params={"status": "available"})
        return [response.status_code, response.reason], response.content



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
