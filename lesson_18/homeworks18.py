import requests as r

base_url = "https://petstore.swagger.io"

new_pet = {
  "id": 8987867656,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "Garphild",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2,
      "name": "lazy"
    }
  ],
  "status": "available"
}

pid = new_pet['id']


def get_list_pets():

    """Find pets with status 'avaible'. Response content type - json with all pets avaible"""

    url = f"{base_url}/v2/pet/findByStatus"
    params = {"status": "available"}
    response = r.get(url, params)
    assert response.status_code == 200
    resp_json = response.json()
    assert len(resp_json), "No pets with status avaible found"
    return resp_json

def create_new_pet(data):

    """ Add new pet to store. Response contains id of added pet"""
    url = f"{base_url}/v2/pet"
    response = r.post(url, json=data)
    assert response.status_code == 200, "Incorrect data format was provided"
    print(f"Pet with id {response.json()['id']} was added successfully")
    return response.json()['id']

def get_pet_by_id(petId):

    """ Get pet by id. Response contains json with pet info"""
    url = f"{base_url}/v2/pet/{petId}"
    response = r.get(url)
    assert response.status_code == 200, "Incorrect id was provided"
    return response.json()

def delete_pet_by_id(petId):

    """ Delete pet by id"""
    url = f"{base_url}/v2/pet/{petId}"
    response = r.delete(url)
    assert response.status_code == 200, "Incorrect id was provided"
    assert int(response.json()['message']) == petId, f"Pet with id {petId} was not deleted"
    print(f"Pet with id {petId} was deleted successfully")


print(get_list_pets())
create_new_pet(new_pet)
print(get_pet_by_id(pid))
delete_pet_by_id(pid)