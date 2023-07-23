import requests
import logging


# base_url = "https://qauto.forstudy.space/api"
# endpoint = "/auth/logout"
# r = requests.get(base_url+endpoint)
# print(r.url)
# print(r.headers)
# print(r.status_code)

# def test_url():
#     r = requests.get(base_url+endpoint)
#     assert r.status_code == 200, f"{r.status_code} is not equal 200"

def test_api_hillel():
    url = "https://qauto.forstudy.space/api-docs/"
    r = requests.get(url, auth=("quest","welcome2qauto"))
    print(r.url)
    print(r.headers)
    print(r.status_code)

test_api_hillel()