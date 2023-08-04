import time

from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageAuth(BasePage):
    def should_be_login(self):
        assert not self.get_element(By.CSS_SELECTOR, 'p.header_bar')

    def should_be_garage_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'a[routerlink="garage"]')

    def should_be_fuel_expenses_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'a[routerlink="expenses"]')

    def should_be_instructions_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'a[routerlink="instructions"]')

    def should_be_profile_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'a[routerlink="profile"]')

    def should_be_settings_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'a[routerlink="settings"]')

    def should_be_logout_btn(self):
        assert self.is_element_present(By.XPATH, '//a [text()=" Log out "]')

    def should_be_add_car_btn(self):
        assert self.is_element_present(By.XPATH, '//button [text()="Add car"]')

    def should_be_elements(self):
        self.should_be_garage_link()
        self.should_be_fuel_expenses_link()
        self.should_be_instructions_link()
        self.should_be_profile_link()
        self.should_be_settings_link()
        self.should_be_logout_btn()
        self.should_be_add_car_btn()

    def click_add_car(self):
        self.get_element(By.XPATH, '//button [text()="Add car"]').click()

    def logout(self):
        self.get_element(By.CSS_SELECTOR, '.dropdown-toggle').click()
        self.get_element(By.CSS_SELECTOR, 'button.dropdown-item').click()