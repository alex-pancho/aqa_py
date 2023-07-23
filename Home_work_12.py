import requests

# Отримати список доступних тварин (метод GET)
url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
get_pets = requests.get(url)
print(get_pets.text)


# Додати нову тварину (метод POST)
new_pet = {"name": "Ly-Ly", "status": "available"}
response = requests.post("https://petstore.swagger.io/v2/pet", json=new_pet)
confirmation = response.json()
pet_id = confirmation["id"]
# Вивести підтвердження про додавання тварини на екран
print(f"New pet added. ID: {confirmation['id']}, Name: {confirmation['name']}")

# Знайти тварину за ідентифікатором (метод GET)
pet_id = confirmation["id"]
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
get_new_pets = requests.get(url)
print(get_new_pets.text)

# Видалити тварину за ідентифікатором (метод DELETE)
pet_id = confirmation["id"]
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
get_delete_pets = requests.delete(url)
print(get_delete_pets.text)

# Обробити відповідь сервера
if response.status_code == 200:
    print(f"Pet with ID {pet_id} has been deleted.")
else:
    print(f"Error deleting pet with ID {pet_id}.")
