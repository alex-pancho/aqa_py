
"Це робочик варіант із статичним шляхом до бінарника гекодрайвера і браузера ФФ"
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

service = Service(r'C:\\webdrivers\\geckodriver.exe')
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.mozilla.org/en-US/firefox/new/")
print(driver.title)
driver.quit()



"Це робочий варіант із автоматичним завантаженням актуальної версії гекодрайвера"
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.mozilla.org/en-US/firefox/new/")
print(driver.title)
driver.quit()