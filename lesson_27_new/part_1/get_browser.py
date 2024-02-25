from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

def firefox(debug=False):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox() if debug else \
             webdriver.Firefox(options=options)
    return driver


def chrome():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options)
    return driver

if __name__ == "__main__":
    driver = firefox()
    # driver = chrome()
    driver.get("http://google.com")
    driver.save_screenshot(r'C:\tp_testing_code\hillel\aqapy\screenshot.png')
    driver.close()
