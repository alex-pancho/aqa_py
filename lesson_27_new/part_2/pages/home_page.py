import sys
import pathlib
root = str(pathlib.Path(__file__).parents[2])
sys.path.insert(0, root)
from pages.elements import WebElement
from pages.base_page import BasePage



class HomePage(BasePage):

    _menu_home = '//a[text()="Home"]'
    _sign_in_button = '//button[.="Sign In"]'
    _contacts_head = '//h2'
    _sign_up_button = '//button[.="Sign Up"]'

    def __init__(self, driver):
        super().__init__(driver)

    def menu_home(self):
        return WebElement(driver=self.driver, xpath=self._menu_home)

    def sign_in_button(self):
        return WebElement(driver=self.driver, xpath=self._sign_in_button)
