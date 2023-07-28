from HW16.objschema.HomePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(HomePage):
    def should_be_login_page(self):
        self.should_be_login_page_name()
        self.should_be_email_form()
        self.should_be_password_form()
        self.should_be_register_link()
        self.should_be_remember_checkbox()
        self.should_be_disabled_login_button()
        self.should_be_close_button()
        self.should_be_forgot_password_btn()

    def should_be_login_page_name(self):
        assert self.is_element_present(By.XPATH, '//h4 [text()="Log in"]')

    def should_be_email_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#signinEmail")
        assert self.is_element_present(By.XPATH, '//label [text()="Email"]')

    def should_be_password_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#signinPassword")
        assert self.is_element_present(By.XPATH, '//label [text()="Password"]')

    def should_be_register_link(self):
        assert self.is_element_present(By.XPATH, '//button [text()="Registration"]')

    def should_be_remember_checkbox(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#remember")

    def should_be_disabled_login_button(self):
        assert self.is_element_present(
            By.XPATH, '//button [text()="Login"] [@disabled]'
        )

    def should_be_enabled_login_button(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button [text()="Login"]'))
        )
        assert button

    def should_be_close_button(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".close")

    def should_be_forgot_password_btn(self):
        assert self.is_element_present(By.XPATH, '//button [text()="Forgot password"]')

    def enter_email(self):
        email_field = self.get_element(By.CSS_SELECTOR, "#signinEmail")
        email_field.send_keys("Test123Test@gmail.com")

    def enter_password(self):
        password_field = self.get_element(By.CSS_SELECTOR, "#signinPassword")
        password_field.send_keys("Q1q2w3eQag")

    def login(self):
        self.enter_email()
        self.enter_password()
        self.should_be_enabled_login_button()
        self.get_element(By.XPATH, '//button [text()="Login"]').click()
        assert not self.is_element_present(By.CSS_SELECTOR, "p.header_bar")
