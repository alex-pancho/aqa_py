from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
url = "https://www.geeksforgeeks.org/action-chains-in-selenium-python/"
driver = webdriver.Firefox()
driver.get(url)
# https://www.selenium.dev/documentation/webdriver/actions_api/
action = ActionChains(driver)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav # submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
