from lesson_28.Tests.elements import WebElement
# Map PageElement constructor arguments to webdriver locator enums
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()


_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("http://www.google.com/")
# print(driver.title)
# driver.quit()

class ForStudy():
    def __init__(self, webdriver, root_uri):
        # self.selenium = selenium
        # self.timeout = timeout
        self.webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.webdriver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
        self.base_ulr = 'https://qauto.forstudy.space'
        self.root_uri = root_uri if root_uri else getattr(self.webdriver, self.root_uri, 'https://qauto.forstudy.space')




class AuthForUser():
    creds = {
        'user_login': 'guest',
        'password': 'welcome2qauto'
    }

    @staticmethod
    def get_url(self, url="https://qauto.forstudy.space"):
        # driver = webdriver.Firefox()
        driver = ForStudy.webdriver
        driver.get(url)
        return driver

    @staticmethod
    def get_signin_for_study_page(user=creds['user_login'], passw=creds['password']):
        return AuthForUser.get_url(f"https://{user}:{passw}@qauto.forstudy.space/")


class PageElement(WebElement):
    def __init__(self, context=False, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def _find_(self, context):
        try:
            return context.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None

        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.webdriver

        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.send_keys(value)


class SpacePageLocators():
    menu_home = '//a[text()="Home"]'
    sign_in_button = '//button[text()="Sign In"]'
    contacts_head = '//h2'
    sign_up_button = '//button[text()="Sign Up"]'


class TestSpacePage(SpacePageLocators):
    webdriver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
    for_study = ForStudy(webdriver, root_uri='https://qauto.forstudy.space')


    def test_home_page_tab_in_headers(self):
        webdriver.get("http://www.google.com/")
        print(webdriver.title)
        webdriver.quit()
        elem1 = WebElement(self.for_study + self.menu_home)
        driver = ForStudy.webdriver
        driver.get("https://qauto.forstudy.space")
        driver.title
        driver.quit()

        print(elem1)
