from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lesson_28.Testing.pages import HomePage
from lesson_28.Testing.project_utils import do_auth_to_forstudy


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


'''TO DO - setup automated validation in tests below later'''
@pytest.fixture
def login_page(driver):
    # Виконуємо відкриття сторінки
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)

    # Vefiry if relevant login page locators is present
    assert home_page.is_element_present(home_page.modal_title_login), "Modal title element not found!"
    assert home_page.is_element_present(home_page.email_input), "Email input element not found!"
    assert home_page.is_element_present(home_page.pswd_input), "Password input element not found!"
    assert home_page.is_element_present(home_page.remember_me_chekbx), "Remember me checkbox element not found!"
    assert home_page.is_element_present(home_page.forgot_pass_btn), "Forgot password button element not found!"
    assert home_page.is_element_present(home_page.registration_btn), "Registration button element not found!"
    assert home_page.is_element_present(home_page.login_btn), "Login button element not found!"

    return home_page


def test_open_login_page(driver):
    '''Verify opening login modal form'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    home_page.click_sign_in_button()
    # Очікуємо на появу модального вікна перед перевіркою
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    assert modal_appeared, "Modal form doesn't exists"


def test_valid_login_and_pass(driver):
    '''Do signin via login form'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)

    # Вхідні дані для тесту
    email = "qam2608@2022test.com"
    password = "Qwerty12345"

    home_page.click_sign_in_button()
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    assert modal_appeared, "Modal form doesn't exists"
    home_page.enter_email(email)
    home_page.enter_password(password)
    home_page.click_login_button()
    """Alternative syntax. Just for information"""
    # email_input =  driver.find_element(*home_page.email_input)
    # password_input = driver.find_element(*home_page.pswd_input)
    # print("password_input>>>>>>>>>>", password_input)
    # email_input.send_keys(email)
    # password_input.send_keys(password)
    # login_btn = driver.find_element(*home_page.login_btn)
    # login_btn.click()

    garage_text_is_present = wait.until(EC.presence_of_element_located(home_page.garage_text_loctr))
    assert garage_text_is_present, "User isn't logged in"


def test_valid_login_via_actionchains(driver):
    '''Do signin via login form using actionchains'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    actions = ActionChains(driver)
    # Вхідні дані для тесту
    email = "qam2608@2022test.com"
    password = "Qwerty12345"

    home_page.click_sign_in_button()
    sleep(3)
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    sleep(3)
    assert modal_appeared, "Modal form doesn't exists"
    email_input = driver.find_element(*home_page.email_input)
    password_input = driver.find_element(*home_page.pswd_input)
    login_btn = driver.find_element(*home_page.login_btn)
    actions.pause(2)
    actions.click(email_input)
    actions.send_keys(email)
    actions.click(password_input)
    actions.send_keys(password)
    actions.click(login_btn)
    actions.perform()
    garage_text_is_present = wait.until(EC.presence_of_element_located(home_page.garage_text_loctr))
    assert garage_text_is_present, "User isn't logged in"


def test_invalid_login_via_actionchains(driver):
    '''Get validation errors in signin form with invalid login using actionchains'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    actions = ActionChains(driver)
    # Вхідні дані для тесту
    email = "q8@test.com"
    password = "Q"

    home_page.click_sign_in_button()
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    assert modal_appeared, "Modal form doesn't exists"
    email_input = driver.find_element(*home_page.email_input)
    password_input = driver.find_element(*home_page.pswd_input)
    login_btn = driver.find_element(*home_page.login_btn)
    actions.pause(2)
    actions.click(email_input)
    actions.send_keys(email)
    actions.click(password_input)
    actions.send_keys(password)
    actions.click(login_btn)
    actions.perform()
    wrong_em_login_allert_is_present = wait.until(EC.presence_of_element_located(home_page.wrong_log_pass_allect_loctr))
    assert wrong_em_login_allert_is_present, "Allert isn't available"


def test_remember_me_checkbox(driver):
    '''Verify cherbox remember me via actionchains'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    actions = ActionChains(driver)
    # Вхідні дані для тесту
    email = None
    password = None

    home_page.click_sign_in_button()
    wait = WebDriverWait(driver, 10)
    modal_appeared = wait.until(EC.presence_of_element_located(home_page.modal_title_login))
    assert modal_appeared, "Modal form doesn't exists"

    # remember_checkbox = driver.find_element(*home_page.remember_me_chekbx)
    actions.pause(2)

    checkbox = wait.until(EC.presence_of_element_located(home_page.remember_me_chekbx))
    assert checkbox, "Checkbox isn't available"

