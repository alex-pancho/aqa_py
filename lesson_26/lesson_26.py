from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_sites(url="http://www.python.org"):
    options = FirefoxOptions()
    # options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Chrome()
    driver.get(url)
    return driver


def search_field(driver):
    element = driver.find_element(By.NAME, "q")
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


if __name__ == "__main__":
    driver = get_sites()
    search_field = search_field(driver)
    invisible_about = invisible_about(driver)
    # check_fields(search_field)
    error_element = error_element(driver)
    # check_fields(error_element)
    expected_field(driver)
