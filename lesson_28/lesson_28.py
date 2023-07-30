from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def work_with_cookies():
    driver = webdriver.Chrome()

    # Navigate to url
    driver.get("http://www.example.com")

    # Adds the cookie into current browser context
    driver.add_cookie({"name": "foo", "value": "bar"})

    # Get cookie details with named cookie 'foo'
    print("по ключу", driver.get_cookie("name"))  # повертає None
    print("по значеню", driver.get_cookie("foo"))  # повертає весь словник
    cookies = driver.get_cookies()[0]
    print("всі кукі", cookies)
    print("по ключу з усіх", cookies["name"])

# work_with_cookies()

def file_uploader(folder, filename = 'some-file.txt'):
    driver = webdriver.Firefox()
    file = str(folder / filename)
    driver.get('http://the-internet.herokuapp.com/upload')
    driver.find_element(By.ID, 'file-upload').send_keys(file)
    driver.find_element(By.ID,'file-submit').click()
    # driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()

    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, "uploaded file should be %s" % filename


def use_wait():
    folder = Path(r"C:\Users\Alex\Pictures\space")
    filename = "238002.jpg"
    file_uploader(folder, filename)

    # Explicit wait == expected явно задані очікування
    driver = webdriver.Firefox()
    WebDriverWait(driver, timeout=10).until("")

    # Implicit wait – приховане очікування
    #  driver.implicitly_wait(10)   ##   КОКТЕЙЛЬ НЕ ПРАЦЮЄ!!!!!!

    # FullentWait
    wait = WebDriverWait(driver,
                         timeout=10,
                         poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException,
                                             ElementNotSelectableException]
                         )
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))


def js_promt():
    url = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"
    driver = webdriver.Firefox()
    driver.get(url)
    # Click the link to activate the alert
    driver.find_element(By.LINK_TEXT, "See an example alert").click()

    # Wait for the alert to be displayed and store it in a variable
    _wait = WebDriverWait(driver, 5)
    alert = _wait.until(EC.alert_is_present())

    # Store the alert text in a variable
    text = alert.text
    print(text)
    # Press the OK button
    # alert.accept()
    # driver.quit()

# js_promt()
# import time
def work_with_windows():
    driver = webdriver.Firefox()
    driver.get('http://the-internet.herokuapp.com/upload')
    driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()
    driver.switch_to.new_window()  # нова пуста вкладка
    driver.switch_to.default_content()  # повинно повертати на перший таб, але не працює
    # time.sleep(2)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)  # перебір табів
    # print(driver.window_handles)
    main_window = driver.window_handles[0]
    driver.switch_to.window(main_window)
    # driver.switch_to.frame("frameName")
    # driver.forward()
    # driver.back()

# work_with_windows()


"https://github.com/seleniumbase/SeleniumBase"