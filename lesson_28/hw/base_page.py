from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url[:8] + 'guest:welcome2qauto@' + self.url[8:])

    def is_element_present(self, method, elem):
        try:
            self.browser.find_element(method, elem)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, method, elem):
        try:
            element = self.browser.find_element(method, elem)
        except NoSuchElementException:
            return False
        return element