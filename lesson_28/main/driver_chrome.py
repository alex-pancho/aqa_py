"Це робочик варіант із статичним шляхом до бінарника chromedriver і браузера Chrome"
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service(executable_path="C:/webdrivers/chromedriver.exe")
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("http://www.google.com/")
# print(driver.title)
# print(driver.current_url)
# print(driver.current_window_handle)
# print(driver.page_source)
# driver.quit()


"Це робочий варіант із автоматичним завантаженням актуальної версії chromedriver"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()


# def chrome_browser():
#     def chmedriver_setup():
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#         return driver
#     return chmedriver_setup()
#
#
# class SpacePageLocators():
#     menu_home = '//a[text()="Home"]'
#     sign_in_button = '//button[text()="Sign In"]'
#     contacts_head = '//h2'
#     sign_up_button = '//button[text()="Sign Up"]'
#
# p_url= '//img[@class="python-logo"]'
#
# def get_sites(url=None):
#     # options = FirefoxOptions()
#     # options.add_argument('-headless')
#     # driver = webdriver.Firefox(options=options)
#     # driver = webdriver.Chrome()
#     chrome_browser.get(url)
#     return driver
#
# if __name__ == '__main__':
#     get_sites(p_url)