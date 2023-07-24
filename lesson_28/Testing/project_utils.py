from selenium import webdriver

# def do_auth_to_forstudy():
#     user = "guest"
#     passw = "welcome2qauto"
#     return webdriver.Chrome(f"https://{user}:{passw}@qauto.forstudy.space/")

from selenium import webdriver

# def do_auth_to_forstudy():
#     user = "guest"
#     passw = "welcome2qauto"
#     url = f"https://{user}:{passw}@qauto.forstudy.space/"
#     return url


def do_auth_to_forstudy(driver):
    user = "guest"
    passw = "welcome2qauto"
    url = f"https://{user}:{passw}@qauto.forstudy.space/"
    driver.get(url)
