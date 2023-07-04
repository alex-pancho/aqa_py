import requests

def pets_stat():
    """Получение список животных"""
    base_url="https://petstore.swagger.io/v2"
    url = base_url + "/pet/findByStatus"
    params = {"status": "available"}

    r=requests.get (url, params=params)

    if r.status_code == 200:
        pets = r.json()
        for pet in pets:
            if 'id' in pet and 'name' in pet and 'status' in pet:
                print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
            else:
                print("Неправильный формат данных для животных")
    else:
        print("Не удалось получить список животных")
pets_stat()

def pets_stat1():
    """Добавление в список животных"""
    url="https://petstore.swagger.io/v2/pet"
    new_pet={"name": "цубака", "status": "available"}
    headers={'Content-Type': 'application/json'}

    response=requests.post (url, json=new_pet, headers=headers)

    if response.status_code == 200:
        print (f"ID: {new_pet['name']} успешно добавлено!")
    else:
        print (f'Не удалось добавить животное. Код ответа: {response.status_code}')
pets_stat1()

def pets_stat4():
    """Получение информации об животном из списка по id"""
    pet_id="111"
    url=f"https://petstore.swagger.io/v2/pet/{pet_id}"
    headers={"Content-Type": "application/json"}

    response=requests.get (url, headers=headers)

    if response.status_code == 200:
        pet_data=response.json ()
        print (f"Информация о питомце: {pet_data}")
    else:
        print (f"Ошибка при выполнении GET-запроса: {response.status_code}")
pets_stat4 ()


def pets_stat5():
    """Удаление животного из списка по id"""
    pet_id="8456911055712932"
    url=f"https://petstore.swagger.io/v2/pet/{pet_id}"
    headers={"Content-Type": "application/json"}

    response=requests.delete (url, headers=headers)

    if response.status_code == 200:
        pet_data=response.json ()
        print (f"Питомец : {pet_id} удален")
    else:
        print (f"Ошибка при выполнении GET-запроса: {response.status_code}")
pets_stat5()
