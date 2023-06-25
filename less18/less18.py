import requests
import js2py 



# url = "https://uakino.club"

# print(r.status_code)
# print(r.status_code)
# print(r.content)
# print(r.text)

# def get_uakino():
#     url = "https://uakino.club"
#     my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
#     # Host: may als be needed

#     req = requests.get(url, headers=my_headers)

#     print(url)
#     print(req.status_code)
#     print(req.headers)

# get_uakino()

#post-installed headers, after login for example

def post_uakino():
    url = "https://uakino.club"
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    my_data = {
        "login_name": "testmad",
        "login_password": "not-a-real-password-lol"
        }

    req = requests.post(url, headers=my_headers, json=my_data)

    print(req.request.body)
    print(req.url)
    # print(req.headers)
    print(req.status_code)
    # print(req.text)

post_uakino()