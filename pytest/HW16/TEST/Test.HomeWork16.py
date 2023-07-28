import pytest
from selenium import webdriver
from HW16.objschema.HomePage import HomePage
from HW16.objschema.car_page import PageCar
from HW16.objschema.login_page import LoginPage
from HW16.objschema.HomePage import HomePage
from HW16.objschema.Main_page import auth_page

BASE_URL = "http://example.com"


@pytest.fixture
def browser():
    """Фікстура для ініціалізації та завершення роботи з браузером."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_main_menu_element(browser):
    """Перевіряє наявність хоча б одного елемента головного меню."""
    main_page = HomePage(browser, BASE_URL)
    main_page.open()
    main_page.should_be_signin_link()


def test_login_form(browser):
    """Перевіряє форму логіна, її заповнення та вхід користувача."""
    login_page = LoginPage(browser, BASE_URL)
    login_page.open()
    login_page.should_be_login_page()
    login_page.enter_email()
    login_page.enter_password()
    login_page.login()
    main_page_auth = auth_page(browser, browser.current_url)
    main_page_auth.should_be_login()


def test_registered_user_menu(browser):
    """Перевіряє меню, що доступне зареєстрованому користувачу."""
    main_page_auth = auth_page(browser, BASE_URL)
    main_page_auth.open()
    main_page_auth.should_be_elements()
    main_page_auth.logout()


def test_add_car_to_garage(browser):
    """Перевіряє додавання машини в гараж для зареєстрованого користувача."""
    login_page = LoginPage(browser, BASE_URL)
    login_page.open()
    login_page.enter_email()
    login_page.enter_password()
    login_page.login()
    main_page_auth = auth_page(browser, browser.current_url)
    main_page_auth.should_be_add_car_btn()
    main_page_auth.click_add_car()
    add_car_page = PageCar(browser, browser.current_url)
    add_car_page.verify_add_car_page_elements()
    add_car_page.choose_brand()
    add_car_page.choose_model()
    add_car_page.input_mileage(10000)
    add_car_page.should_display_enabled_add_button()
    add_car_page.add_car()
    main_page_auth.logout()


def test_contacts_on_homepage(browser):
    """Перевіряє наявність контактів з компанією на головній сторінці."""
    main_page = HomePage(browser, BASE_URL)
    main_page.open()
    main_page.should_be_contacts_footer()


def test_all_page_objects(browser):
    """Перевіряє всі об'єкти на сторінці: головне меню, форму логіна та додавання машини в гараж."""
    main_page = HomePage(browser, BASE_URL)
    main_page.open()
    main_page.should_be_navbar_links()
    main_page.play_video()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.enter_email()
    login_page.enter_password()
    login_page.login()

    main_page_auth = auth_page(browser, browser.current_url)
    main_page_auth.should_be_elements()
    main_page_auth.click_add_car()

    add_car_page = PageCar(browser, browser.current_url)
    add_car_page.verify_add_car_page_elements()
    add_car_page.choose_brand()
    add_car_page.choose_model()
    add_car_page.input_mileage(10000)
    add_car_page.should_display_enabled_add_button()
    add_car_page.add_car()

    main_page_auth.logout()
