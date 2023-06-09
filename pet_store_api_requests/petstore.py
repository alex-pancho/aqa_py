import requests

class Petstore():
    base_url = "http://petstore.swagger.io/v2"

    def get_request_debug_info(self, url_path):
        print(requests.codes)
        print(requests.url)
        print(f"Request body: {requests.request.body}")

    # def get_petstore_status(self, user_prompt:str = "pending"):
    #     '''Get pets status. Default:status:pending'''
    #     pet_findstatus_path_param = "/pet/findByStatus"
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    #     }
    #     pet_status_codes = ["pending", "available", "sold"]
    #
    #
    #     user_prompt = input("To get pets status print: pending, available or sold:")
    #     if user_prompt == pet_status_codes[0]:
    #         r = requests.get("http://petstore.swagger.io/v2" + pet_findstatus_path_param, headers=headers, params={"status": "pending"})
    #         print("Server status response:", r.status_code)
    #         print("Server response in json format:",r.json())
    #     elif user_prompt == pet_status_codes[1]:
    #         r = requests.get("http://petstore.swagger.io/v2" + pet_findstatus_path_param,params={"status": "available"})
    #         print("Server status response:", r.status_code)
    #         print("Server response in json format:", r.json())
    #     elif user_prompt == pet_status_codes[2]:
    #         r = requests.get("http://petstore.swagger.io/v2" + pet_findstatus_path_param,params={"status": "sold"})
    #         print("Server status response:", r.status_code)
    #         print("Server response in json format:", r.json())
    #
    #     return r

    def get_petstore_status(self):
        '''Get pets status. Default:status:pending'''
        pet_findstatus_path_param = "/pet/findByStatus"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        pet_status_codes = ["pending", "available", "sold"]

        user_prompt = input("To get pets status, print: pending, available, or sold: ")
        if user_prompt not in pet_status_codes:
            false_prompt = user_prompt
            raise ValueError(f"Your input is:<{false_prompt}>,  doesn't match of {pet_status_codes}. Try again")

        params = {"status": user_prompt}
        url = self.base_url + pet_findstatus_path_param

        r = requests.get(url, headers=headers, params=params)
        print("Server status response:", r.status_code)
        print("Server response in json format:", r.json())



    def create_pet(self, name:str, status:str):
    '''Додати нову тварину (метод POST).
    Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.
    Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.
    Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.'''




if __name__ == "__main__":
    petstore = Petstore()
    petstore.get_petstore_status()

