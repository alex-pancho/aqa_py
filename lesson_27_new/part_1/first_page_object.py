from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self, driver, url):
        self.driver = driver
        self.page = self.driver.get(url)
        if "Login Example" not in driver.title:
            raise ValueError(
                "This is not Sign In Page, current page is: " +
                driver.current_url)

    username_by = (By.NAME, "email")
    password_by = (By.NAME, "password")
    signin_by = (By.XPATH, '//form//div[.="Login"]')

    def login_valid_user(self, username, password):
        self.driver.find_element(*self.username_by).send_keys(username)
        self.driver.find_element(*self.password_by).send_keys(password)
        self.driver.find_element(*self.signin_by).click()
        return HomePage(self.driver)


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # if "Home Page of logged in user" not in driver.title:
        #     raise ValueError(
        #         "This is not Home Page of logged in user, current page is: " +
        #         driver.current_url)

    message_by = (By.TAG_NAME, "h2")

    def get_message_text(self):
        return self.driver.find_element(*self.message_by).text

    def manage_profile(self):
        # Page encapsulation to manage profile functionality
        return HomePage(self.driver)
