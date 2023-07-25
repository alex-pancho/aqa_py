from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lesson_28.Testing.pages import HomePage
from lesson_28.Testing.elements import WebElement
from lesson_28.Testing.project_utils import do_auth_to_forstudy
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('-headless')
    driver = webdriver.Chrome(options=options)
    # Авторизуємося на сторінці перед кожним тестом
    do_auth_to_forstudy(driver)  # Передаємо браузер driver до функції do_auth_to_forstudy
    yield driver
    # Закриваємо браузер після кожного тесту
    driver.quit()

def test_add_car_to_garage(driver):
    '''add veihile to garage'''
    url = 'https://qauto.forstudy.space/panel/garage'
    home_page = HomePage(driver, url=url)
    actions = ActionChains(driver)

    # Вхідні дані для тесту
    email = "qam2608@2022test.com"
    password = "Qwerty12345"
    num_mileage = 10

    home_page.click_sign_in_button()
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    assert modal_appeared, "Modal form doesn't exists"
    home_page.enter_email(email)
    home_page.enter_password(password)
    home_page.click_login_button()
    wait = WebDriverWait(driver, 10)
    garage_text_is_present = wait.until(EC.presence_of_element_located(home_page.garage_text_loctr))
    assert garage_text_is_present, "User isn't logged in"
    home_page.click_add_car_button()

    mileage_input = driver.find_element(*home_page.mileage_input)
    add_car_modal_btn = driver.find_element(*home_page.add_car_modal_btn)

    actions.pause(2)
    actions.click(mileage_input).send_keys(2)
    actions.pause(2)

    actions.click(add_car_modal_btn)
    # actions.pause(2)
    # add_car_btn = driver.find_element(*home_page.add_car_btn)
    # actions.click(add_car_btn)
    # actions.pause(2)
    actions.perform()
