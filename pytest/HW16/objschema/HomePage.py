from selenium.common.exceptions import NoSuchElementException


class HomePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url[:8] + "guest:welcome2qauto@" + self.url[8:])

    def is_element_present(self, locator_method, locator):
        try:
            self.browser.find_element(locator_method, locator)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, locator_method, locator):
        try:
            element = self.browser.find_element(locator_method, locator)
        except NoSuchElementException:
            return None
        return element
