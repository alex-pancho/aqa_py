import requests


def get_google():
    base_url = "https://www.google.com"
    r = requests.get(base_url+"/search", params={"q": "школа ліцей"})
    print(r.url)
    print(r.headers)
    print(r.status_code)
    #print(r.text) #  r.content


def get_olx(vid:int = 10, do:int = 100):
    base_url = "https://www.olx.ua"
    r = requests.get("/".join([base_url, "d", "uk", "q-вермишель"]),
                     params={"currency": "UAH",
                             "search[filter_float_price:from]": vid,
                             "search[filter_float_price:to]": do})
    print(r.url)
    print(r.headers)
    print(r.status_code)
    #print(r.text) #  r.content


# get_olx(1, 25)

def test_api_hillel():
    url = "https://qauto.forstudy.space/api-docs/"
    r = requests.get(url, auth=("guest", "welcome2qauto"))
    print(r.url)
    print(r.headers)
    print(r.status_code)
    print(r.text)


# test_api_hillel()


def get_uakino():
    url = "https://uakino.club"
    headers = {
        "Host": "uakino.club",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }

    r = requests.get(url, headers=headers)

    print(r.url)
    print(r.headers)
    print(r.status_code)


# get_uakino()


def post_uakino():
    base_url = "https://uakino.club"
    headers = {
        "Host": "uakino.club",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }

    data = {
        "login_name": "panix",
        "login_password": "myPa$$w0rd",
        "login": "submit"
    }

    url = base_url
    r = requests.post(url, headers=headers, json=data)
    print("request body:", r.request.body)
    print("request headers:", r.request.headers)
    print("request url:", r.request.url)
    print("===")
    print(r.url)
    print(r.headers)
    print(r.status_code)
    # print(r.text)
    # print(r.json())


# post_uakino()
from requests.auth import HTTPProxyAuth
def test_api_hillel_2():
    base_url = "https://qauto.forstudy.space/api"
    url = base_url + "/auth/signup"
    data = {
        "name": "John",
        "lastName": "Dou",
        "email": "test8@test.com",
        "password": "Qwerty12345",
        "repeatPassword": "Qwerty12345"
        }
    #proxy = {"http":"username@password@proxyip:port"}
    proxy = {"http":"192.168.20.130:8080"}
    auth = HTTPProxyAuth("username", "password")
    r = requests.post(url, json=data, proxies=proxy, auth=auth)
    print(r.url)
    print(r.headers)
    print(r.status_code)
    print(r.json()) # try except


test_api_hillel_2()
