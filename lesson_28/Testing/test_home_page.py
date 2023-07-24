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


def test_click_about_btn(driver):
    '''do click About menu'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    # Перевіряємо, чи була здійснена переадресація на правильну сторінку
    expected_url = 'https://qauto.forstudy.space/'
    assert expected_url == url, f"Incorrect url. Expected <{expected_url}>, Actual <{url}>"
    # Перевіряємо, чи можна натиснути на елемент "Home"
    elem = WebElement(xpath=home_page.about_btn_locator[1])
    assert elem._locator == home_page.about_btn_locator, "Locator doesn't match with initial HomePage locator"

    try:
        wait = WebDriverWait(driver, 3)
        clickable_elem = wait.until(EC.element_to_be_clickable(HomePage.about_btn_locator))
        # print("Status clickable Element:", clickable_elem) інфо для дебага статусу елемента або екземп.елемента
        if clickable_elem:
            clickable_elem.click()
        else:
            raise NoSuchElementException("Element isn't clickable")
    except NoSuchElementException as e:
        # ...
        raise e


def test_clickable_home_menu(driver):
    '''verify if clickable home menu tab'''
    url = 'https://qauto.forstudy.space/'
    home_page = HomePage(driver, url=url)
    wait = WebDriverWait(driver, 3)
    is_clickable = wait.until(EC.element_to_be_clickable(HomePage.menu_home))
    # If the element is clickable, click it
    if is_clickable:
        home_page.click_home_menu()
    else:
        assert False, "Element isn't clickable"


def test_text_contact(driver):
    '''test text in contact locator'''
    home_page = HomePage(driver, url='https://qauto.forstudy.space')
    contacts_head_element = driver.find_element(*home_page.contacts_head)
    actual_res = contacts_head_element.text
    expected_res = 'Contacts'
    assert expected_res == actual_res, f"Actual text <{actual_res}> doesn't match to expected text <{expected_res}>"
    assert contacts_head_element.is_displayed(), "Element isn't displayed"

#команда для запуску в терміналі формування xml репортінгу:pytest -rA --junit-xml="JUnitXmlReport.xml"
