import requests


def get_available_pets():
    """Отримати список доступних тварин"""
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    params = {'status': 'available'}
    r = requests.get(url, params=params)

    if r.status_code == 200:
        pets = r.json()
        for pet in pets:
            if 'id' in pet and 'name' in pet and 'status' in pet:
                print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
            else:
                print('Неправильний формат даних для тварини')
    else:
        print('Не вдалося отримати список тварин')
 

def add_new_pet(name, status):
    """Додаємо нову тваринку"""
    url = 'https://petstore.swagger.io/v2/pet'
    headers = {'Content-Type': 'application/json'}
    data = {
        'name': name,
        'status': status
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        pet = response.json()
        print(f"Тварину з ID {pet['id']} було успішно додано")
    else:
        print('Не вдалося додати нову тварину')


def find_pet_by_id(pet_id):
    """Пошук тварини по id"""
    url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
    response = requests.get(url)

    if response.status_code == 200:
        pet = response.json()
        print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print('Тварину не знайдено')


def delete_pet_by_id(pet_id):
    """Видалення тварини по id"""
    url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
    response = requests.delete(url)

    if response.status_code == 200:
        print(f"Тварину з ID {pet_id} було успішно видалено")
    else:
        print('Не вдалося видалити тварину')


#get_available_pets()  # вивели список тварин

#add_new_pet('Dina', 'available')  # додали тварину

#find_pet_by_id() # пошук тварини за id, яку ми створили у функції add_new_pet()

#delete_pet_by_id() # видалення цієї тварини


