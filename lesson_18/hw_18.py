import requests

def get_available_pets():
    """Get list of available pets"""
    try:
        response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
        response.raise_for_status()
        pets = response.json()

        pet_info = []
        for pet in pets:
            pet_info.append({
                'id': pet['id'],
                'name': pet['name'],
                'status': pet['status']
            })

        return pet_info

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def add_new_pet(name, status, id):
    """add new pet with name, status and id"""
    try:
        pet_data = {
            'name': name,
            'status': status,
            'id' : id
        }

        response = requests.post('https://petstore.swagger.io/v2/pet', json=pet_data)
        response.raise_for_status()

        return "New pet added successfully."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def find_pet_by_id(pet_id):
    """search pets by id"""
    try:
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

        response = requests.get(url)
        response.raise_for_status()

        pet = response.json()
        pet_info = {
            'id': pet['id'],
            'name': pet['name'],
            'status': pet['status']
        }

        return pet_info

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def delete_pet_by_id(pet_id):
    """delete pet """
    try:
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

        response = requests.delete(url)
        response.raise_for_status()

        return "Pet deleted successfully."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Приклад використання функцій
    available_pets = get_available_pets()
    if isinstance(available_pets, list):
        for pet in available_pets:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(available_pets)

    print(add_new_pet("Fluffy", "available", 876666))

    pet_id = 876666  # Id тварини для пошуку і видалення, взятий з того що ми створюємо
    pet_info = find_pet_by_id(pet_id)
    if isinstance(pet_info, dict):
        print(f"ID: {pet_info['id']}, Name: {pet_info['name']}, Status: {pet_info['status']}")
    else:
        print(pet_info)

    print(delete_pet_by_id(pet_id))