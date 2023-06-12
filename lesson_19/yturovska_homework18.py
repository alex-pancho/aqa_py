import requests

base_url = "https://petstore.swagger.io/v2"

add_pet_data = {
            "id": 123456789987654321,
            "category": {
                "id": 123456789987654321,
                "name": "Sobaka-Barabaka"
            },

            "status": "available"
        }

pet_id = add_pet_data['id']
pet_name = add_pet_data['category']['name']


def get_pets():

    """Searching for pets with "available" status"""

    url = base_url + "/pet/findByStatus/"
    resp = requests.get(url, params={"status": "available"})
    assert resp.status_code == 200
    return resp.status_code, resp.json()

def post_pet(add_pet_data):

    """New pet creating"""

    url = base_url + "/pet"
    resp = requests.post(url, json=add_pet_data)
    assert resp.status_code == 200, "Incorrect data was provided(endpoint/pet data/etc...)"
    print(f"The pet with name {resp.json()['category']['name']}, and ID {resp.json()['id']} was added")
    return resp.status_code, resp.json()



def get_pet_ID(pet_id):

    """Get pet by ID"""

    url = f"{base_url}/pet/{pet_id}"
    resp = requests.get(url)
    print("status code:", resp.status_code)
    assert resp.status_code == 200, "Incorrect search data(e.g. pet ID)"
    print(f"The pet with ID {pet_id} is found")
    return resp.status_code, resp.json()


def delete_pet_ID(pet_id):

    """Delete pet by ID"""

    url = f"{base_url}/pet/{pet_id}"
    resp = requests.delete(url)
    assert resp.status_code == 200, "Incorrect search data(e.g. pet ID)"
    print(f"The pet with pet ID {pet_id} was deleted")
    return resp.status_code, resp.json()



print(get_pets())
post_pet(add_pet_data)
print(get_pet_ID(pet_id))
delete_pet_ID((pet_id))
#get_pet_ID(pet_id)










