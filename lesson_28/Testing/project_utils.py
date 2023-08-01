import random


def do_auth_to_forstudy(driver):
    '''form driver for access to site https://qauto.forstudy.space'''
    user = "guest"
    passw = "welcome2qauto"
    url = f"https://{user}:{passw}@qauto.forstudy.space/"
    driver.get(url)


def generate_random_number():
    # Генеруємо випадкове str(число від 1 до 100000)
    return str(random.randint(1, 10000))
