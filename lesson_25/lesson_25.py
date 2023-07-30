from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_python(url="http://www.python.org"):
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_hillel_test(user="guest", passw="welcome2qauto"):
    return get_python(f"https://{user}:{passw}@qauto.forstudy.space/")


def main_menu_about(driver):
    element = driver.find_element(By.ID, "about")
    return element


def search_field(driver):
    element = driver.find_element(By.NAME, "q")
    return element


def found_results(driver):
    element = driver.find_element(By.XPATH,
                                  '//ul[@class="list-recent-events menu"]/p')
    return element


def click_on(element):
    element.click()


def input_to(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


def get_text(element):
    return element.text


if __name__ == "__main__":
    window = get_python()
    element = main_menu_about(window)
    # click_on(element)
    elem2 = search_field(window)
    input_to(elem2, "int")
