from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver_manager.chrome import ChomeDriverManager

from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from main import WebElement, ManyWebElements


chrome_browser = Chrome(executable_path="C:\webdrivers")
chrome_browser_2 = Chrome(executable_path="C:\webdrivers")
firefox_browser = Firefox(executable_path=GeckoDriverManager().install())

class SpacePageLocators():
    menu_home = '//a[text()="Home"]'
    sign_in_button = '//button[text()="Sign In"]'
    contacts_head = '//h2'
    sign_up_button = '//button[text()="Sign Up"]'


def get_sites(url="http://www.python.org"):
    options = FirefoxOptions()
    # options.add_argument('-headless')
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def search_field(driver):
    element = driver.find_element(By.XPATH, '//img[@class="python-logo"]')
    # print(element.get_attribute(name="python"))
    return element


# def set_headers(driver, url):
#     REMOTE WEBDRIVER ONLY
#     https://selenium-python.readthedocs.io/api.html?highlight=desired_capabilities#selenium.webdriver.remote.webdriver.WebDriver.desired_capabilities
#     desired_capabilities = DesiredCapabilities.FIREFOX.copy()
#     desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Ukrainian new Browser'
#     driver = webdriver.Firefox(desired_capabilities=desired_capabilities)
#     driver.get(url)


def check_fields(element):
    try:
        result = element.is_displayed()
    except (NoSuchElementException, AttributeError):
        result = False
    try:
        result2 = element.is_enabled()
    except (NoSuchElementException, AttributeError):
        result2 = False
    print("element is displayed", result)
    print("element is enabl", result2)


def invisible_about(driver):
    xpath = '//li[@id="about"]//a[@href="/about/apps/"]'
    element = driver.find_element(By.XPATH, xpath)
    return element


class FalseElement():

    def is_displayed(self):
        return False

    def is_enabled(self):
        return False


def error_element(driver):
    xpath = '//li[@id="ewuygeb"]'

    try:
        element = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        element = False # FalseElement()
    return element

def expected_nf_field(driver):
    xpath = '//li[@id="ewuygeb"]'
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")
    finally:
        driver.quit()


def expected_field(driver):
    xpath = '//*[@name="q"]'
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )  # наявність поля
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )  # чи клікабельне
        driver.save_screenshot(r'C:\tp_testing_code\hillel\aqapy\screenshot.png')
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")
    finally:
        driver.quit()


def main_menu_about(driver):
    element = driver.find_element(By.ID, "about")
    return element

def get_python(url="http://www.python.org"):
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_hillel_test(user="guest", passw="welcome2qauto"):
    driver = webdriver.Chrome()
    driver.get(f"https://{user}:{passw}@qauto.forstudy.space/")
    print(driver)
    return driver



if __name__ == "__main__":
    driver = get_sites()
    search_field = search_field(driver)
    invisible_about = invisible_about(driver)
    check_fields(search_field)
    error_element = error_element(driver)
    # check_fields(error_element)
    expected_field(driver)
    get_hillel_test()
    print(search_field)
