from time import sleep

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lesson_28.Testing.elements import WebElement
from lesson_28.Testing.pages import HomePage
from lesson_28.Testing.project_utils import do_auth_to_forstudy


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    # Авторизуємося на сторінці перед кожним тестом
    do_auth_to_forstudy(driver)  # Передаємо браузер driver до функції do_auth_to_forstudy
    yield driver
    # Закриваємо браузер після кожного тесту
    driver.quit()


def test_open_login_page(driver):
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    home_page.click_sign_in_button()
    # Очікуємо на появу модального вікна перед перевіркою
    home_page.wait_for_modal_login_to_appear()
    sleep(2)
    # Перевірка, чи елемент присутній на модалці
    # elem = WebElement(xpath=home_page.modal_title_login[1])
    elem = WebElement(xpath='//h4[text()="Log in"]')
    print("More info about variable elem>>>", elem)
    is_present = elem.is_presented()
    assert is_present, "Елемент не знайдено на сторінці!"

    # Перевірка, чи відкривається сторінка логіну
    # elem = WebElement(xpath=home_page.sign_in_button[1])
    # wait = WebDriverWait(driver, 3)
    # clickable_elem = wait.until(EC.element_to_be_clickable(HomePage.sign_in_button))
    # sleep(3)
    # assert clickable_elem.click(), "Modal form doesn't exists"
