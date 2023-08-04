import time

from main_page import MainPage
from login_page import LoginPage
from main_page_auth import MainPageAuth
from add_car_page import AddCarPage
from selenium.webdriver.common.by import By

LINK = 'https://qauto.forstudy.space/'


def test_signin_is_present(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_signin_link()


def test_navbar_elements_is_present(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_navbar_links()


def test_contacts_in_footer_is_present(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_navbar_links()


def test_open_signin_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.should_be_login_page()


def test_login(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.login()
    assert browser.current_url == "https://guest:welcome2qauto@qauto.forstudy.space/panel/garage"


def test_user_auth_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.login()
    auth_page = MainPageAuth(browser, browser.current_url)
    auth_page.should_be_login()
    auth_page.should_be_elements()


def test_open_add_car_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.login()
    auth_page = MainPageAuth(browser, browser.current_url)
    auth_page.click_add_car()
    add_car_page = AddCarPage(browser, browser.current_url)
    add_car_page.add_car_start_page_elements()


def test_add_car(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.login()
    auth_page = MainPageAuth(browser, browser.current_url)
    auth_page.click_add_car()
    add_car_page = AddCarPage(browser, browser.current_url)
    add_car_page.add_car()


def test_logout(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_signin_page()
    signin_page = LoginPage(browser, browser.current_url)
    signin_page.login()
    auth_page = MainPageAuth(browser, browser.current_url)
    auth_page.logout()
    time.sleep(2)
    assert browser.current_url == 'https://guest:welcome2qauto@qauto.forstudy.space/'


def test_guest_login(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.guest_login()
    assert browser.current_url == 'https://guest:welcome2qauto@qauto.forstudy.space/panel/garage'
    assert browser.find_element(By.CSS_SELECTOR, 'p.header_bar')