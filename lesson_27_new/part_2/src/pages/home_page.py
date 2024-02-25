from elements import WebElement
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    _search = (By.NAME, "search")
    _menu_home = '//a[text()="Home"]'
    _sign_in_button = '//button[.="Sign In"]'
    _contacts_head = '//h2'
    _sign_up_button = '//button[.="Sign Up"]'

    def __init__(self, driver):
        super().__init__(driver)

    def search(self):
        return WebElement(_search=self._search)

    def sign_in_button(self):
        return WebElement(_sign_in_button=(By.XPATH, self._sign_in_button))
