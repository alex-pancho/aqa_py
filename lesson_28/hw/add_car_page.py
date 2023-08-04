from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCarPage(BasePage):
    def add_car_start_page_elements(self):
        self.should_be_add_car_name_page()
        self.should_be_close_btn()
        self.should_be_brand_selector()
        self.should_be_model_selector()
        self.should_be_mileage_input()
        self.should_be_cancel_btn()
        self.should_be_disabled_add_btn()

    def should_be_add_car_name_page(self):
        assert self.is_element_present(By.XPATH, '//h4 [text()="Add a car"]')

    def should_be_close_btn(self):
        assert self.is_element_present(By.CSS_SELECTOR, '.close span')

    def should_be_brand_selector(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#addCarBrand')

    def should_be_model_selector(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#addCarModel')

    def should_be_mileage_input(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#addCarMileage')

    def should_be_cancel_btn(self):
        assert self.is_element_present(By.XPATH, '//button [text()="Cancel"]')

    def should_be_disabled_add_btn(self):
        assert self.is_element_present(By.XPATH, '//button [text()="Add"] [@disabled]')

    def choose_brand(self, brand='BMW'):
        """current present brands: Audi, BMW, Ford, Porsche, Fiat"""
        self.get_element(By.CSS_SELECTOR, '#addCarBrand').click()
        self.get_element(By.XPATH, f'//select [@id="addCarBrand"]//option [text()="{brand}"]').click()

    def choose_model(self, num=1):
        """num - it is model number in dropdown list, can be from 1 to 5"""
        self.get_element(By.CSS_SELECTOR, '#addCarModel').click()
        self.get_element(By.CSS_SELECTOR, f'#addCarModel option:nth-child({str(num)})').click()

    def input_mileage(self, num=0):
        """num can be only positive from 0 to 999999"""
        self.get_element(By.CSS_SELECTOR, '#addCarMileage').send_keys(f'{str(num)}')

    def should_be_enabled_add_button(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button [text()="Add"]')))
        assert button

    def add_car(self, brand='BMW', model=1, mileage=0):
        self.choose_brand(brand)
        self.choose_model(model)
        self.input_mileage(mileage)
        self.should_be_enabled_add_button()
        self.get_element(By.XPATH, '//button [text()="Add"]').click()
        assert self.is_element_present(By.CSS_SELECTOR, '.car_logo')