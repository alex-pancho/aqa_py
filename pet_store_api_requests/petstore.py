import requests

class Petstore():
    base_url = "https://petstore.swagger.io/v2"
    pet_status_codes = ["pending", "available", "sold"]

    def print_server_response(self, r):
        '''Print response information'''
        print("<---")
        print("Server status response:", r.status_code)
        print("Server response in json format:", r.json())
        print("--->")


    def get_petstore_status(self):
        '''Get pets status in petstore'''
        pet_findstatus_path_param = "/pet/findByStatus"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        user_prompt = input("To get pets status, print: pending, available, or sold: ")
        try:
            if user_prompt not in self.pet_status_codes:
                raise ValueError(f"Your input is:<{user_prompt}>, doesn't match {self.pet_status_codes}. Try again")

            params = {"status": user_prompt}
            url = self.base_url + pet_findstatus_path_param

            r = requests.get(url, headers=headers, params=params)
            self.print_server_response(r)
        except ValueError as e:
            print(e)


    def add_pet_to_store(self, name:str, status:str):
        '''Додати нову тварину (метод POST).
        Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.
        Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.
        Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.'''

        pet_create_path_param = "/pet"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        data = {
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": status
        }
        try:
            if len(name)== 0 or len(status)== 0:
                raise ValueError(f"Your send empty parametr:name<{name}> or status<{status}>. Empty str name or status are prohibited. Try again!")
            if status not in self.pet_status_codes:
                raise ValueError(f"You send invalid paramet:status<{status}>. Remainder! Valid status list:{self.pet_status_codes}. Try again")
            url = self.base_url + pet_create_path_param
            r = requests.post(url, headers=headers, json=data)
            self.print_server_response(r)
            json_response = r.json()
            pet_name = json_response["name"]
            pet_status = json_response["status"]
            pet_id = json_response["id"]
            print(f"Response name is <{pet_name}> and status is <{pet_status}>")
            # print(f"Response id<{pet_id}>")

        except ValueError as e:
            print(e)



    def find_pet_by_id(self):
        '''Знайти тварину за ідентифікатором (метод GET).
        Введіть ідентифікатор тварини, яку потрібно знайти.
        Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.
        Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.'''
        pet_findstatus_path_param = "/pet/findByStatus"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        user_prompt = input("To get pets status, print: pending, available, or sold: ")
        try:
            if user_prompt not in self.pet_status_codes:
                raise ValueError(f"Your input is:<{user_prompt}>, doesn't match {self.pet_status_codes}. Try again")

            params = {"status": user_prompt}
            url = self.base_url + pet_findstatus_path_param

            r = requests.get(url, headers=headers, params=params)
            self.print_server_response(r)
        except ValueError as e:
            print(e)

        pass





if __name__ == "__main__":
    petstore = Petstore()
    # petstore.get_petstore_status()
    petstore.add_pet_to_store("t", "pending")

