from HW16.objschema.HomePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCar(HomePage):
    def verify_add_car_page_elements(self):
        self.should_display_add_car_title()
        self.should_display_close_button()
        self.should_display_brand_selector()
        self.should_display_model_selector()
        self.should_display_mileage_input()
        self.should_display_cancel_button()
        self.should_display_disabled_add_button()

    def should_display_add_car_title(self):
        assert self.is_element_present(By.XPATH, '//h4[text()="Add a car"]')

    def should_display_close_button(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".close span")

    def should_display_brand_selector(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#addCarBrand")

    def should_display_model_selector(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#addCarModel")

    def should_display_mileage_input(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#addCarMileage")

    def should_display_cancel_button(self):
        assert self.is_element_present(By.XPATH, '//button[text()="Cancel"]')

    def should_display_disabled_add_button(self):
        assert self.is_element_present(By.XPATH, '//button[text()="Add"][@disabled]')

    def choose_brand(self, brand="BMW"):
        """Available brands: Audi, BMW, Ford, Porsche, Fiat"""
        self.get_element(By.CSS_SELECTOR, "#addCarBrand").click()
        self.get_element(
            By.XPATH, f'//select[@id="addCarBrand"]//option[text()="{brand}"]'
        ).click()

    def choose_model(self, num=1):
        """num - model number in the dropdown list, can be from 1 to 5"""
        self.get_element(By.CSS_SELECTOR, "#addCarModel").click()
        self.get_element(
            By.CSS_SELECTOR, f"#addCarModel option:nth-child({str(num)})"
        ).click()

    def input_mileage(self, num=0):
        """num can be only positive from 0 to 999999"""
        self.get_element(By.CSS_SELECTOR, "#addCarMileage").send_keys(f"{str(num)}")

    def should_display_enabled_add_button(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Add"]'))
        )
        assert button

    def add_car(self, brand="BMW", model=1, mileage=0):
        self.choose_brand(brand)
        self.choose_model(model)
        self.input_mileage(mileage)
        self.should_display_enabled_add_button()
        self.get_element(By.XPATH, '//button[text()="Add"]').click()
        assert self.is_element_present(By.CSS_SELECTOR, ".car_logo")
