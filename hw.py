import requests


class Pet:

    BaseUrl = 'https://petstore.swagger.io/v2/pet'

    @staticmethod
    def checker(response):
        """Check response on valid"""
        try:
            response.raise_for_status()
            try:
                response.json()
            except requests.JSONDecodeError():
                return 'Response body is not JSON format'
        except requests.HTTPError:
            return response.status_code, response.reason
        else:
            return response.json()

    def get_available_pets(self):
        """Get list with pets"""
        response = requests.get('/'.join([Pet.BaseUrl, 'findByStatus']), params={'status': 'available'})
        return self.checker(response)

    def add_pet(self, data):
        """Add new pet"""
        response = requests.post(Pet.BaseUrl, json=data)
        return self.checker(response)

    def get_pet(self, value: int | str):
        """Find pet by id"""
        response = requests.get('/'.join([Pet.BaseUrl, str(value)]))
        return self.checker(response)

    def delete_pet(self, value: int | str):
        """Delete pet BibleThump :,( """
        response = requests.delete('/'.join([Pet.BaseUrl, str(value)]))
        return self.checker(response)


# Дані для додаваної тварини
new_pet = {
    'name': 'Zhabenyatko',
    'status': 'available'
}

# Створюємо екземпляр класу
p = Pet()

# Отримуємо перелік тварин за статусом наявності
print(p.get_available_pets())

# Додаємо нову тварину, збережемо її до змінної, щоб мати доступ до її id
created_pet = p.add_pet(new_pet)
print(created_pet)

# Отримуємо id будь-якої тварини (для прикладу візьмемо існуючий зі створеної вище тварини та неіснуючий)
print(p.get_pet(created_pet['id']))
print(p.get_pet(12345))

# Видаляємо тварину за її id (для прикладу візьмемо існуючий зі створеної вище тварини та неіснуючий)
print(p.delete_pet(created_pet['id']))
print(p.delete_pet(12345))
