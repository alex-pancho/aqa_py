class BasePage:

    common_locator = '//h1'

    def __init__(self, driver):
        self.driver = driver
