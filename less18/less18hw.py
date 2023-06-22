import requests

base_url = "https://petstore.swagger.io/v2"

def get_all_pets_by_all_statuses():
    r = requests.get(base_url+"/pet/findByStatus/", 
                     params={"status":"available",
                             "status":"pending",
                             "status":"sold"})
    if r.status_code == 200:
        print("Success")
        print(r._content)
    else:
        print ("Something went wrong. Status code:", r.status_code)


def create_new_pet():
    new_pet_data = {"id":70999,
            "name":"coolPet",
            "status":"pending"}
    
    r = requests.post(base_url+"/pet", json=new_pet_data)

    if r.status_code == 200:
        print("Success")
        print(r._content)
    else:
        print ("Something went wrong. Status code:", r.status_code)

def get_pet_by_id(petId):

    r = requests.get(base_url+"/pet/"+petId)

    if r.status_code == 200 or r.status_code == 201: #may be expected 201, but for now server responds with 200
        print("Success")
        print(r._content)
    else:
        print ("Something went wrong. Status code:", r.status_code)

def delete_pet_by_id(petId):

    r = requests.delete(base_url+"/pet/"+petId)

    if r.status_code == 200:
        print("Success")
        print(r._content)
    else:
        print ("Something went wrong. Status code:", r.status_code)

get_all_pets_by_all_statuses()
create_new_pet()
get_pet_by_id("70999")
delete_pet_by_id("70999")
