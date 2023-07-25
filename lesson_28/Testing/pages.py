#!/usr/bin/python3
# -*- encoding=utf8 -*-

# from elements import WebPage

# from selenium.webdriver.common.by import WebElement
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# class WebPage(object):
#
#     _web_driver = None
#
#     def __init__(self, web_driver, url=''):
#         self._web_driver = web_driver
#         self.get(url)
#
#     def __setattr__(self, name, value):
#         if not name.startswith('_'):
#             self.__getattribute__(name)._set_value(self._web_driver, value)
#         else:
#             super(WebPage, self).__setattr__(name, value)
#
#     def __getattribute__(self, item):
#         attr = object.__getattribute__(self, item)
#
#         if not item.startswith('_') and not callable(attr):
#             attr._web_driver = self._web_driver
#             attr._page = self
#
#         return attr
#
#     def get(self, url):
#         self._web_driver.get(url)
#         self.wait_page_loaded()
#
#     def go_back(self):
#         self._web_driver.back()
#         self.wait_page_loaded()
#
#     def refresh(self):
#         self._web_driver.refresh()
#         self.wait_page_loaded()
#
#     def screenshot(self, file_name='screenshot.png'):
#         self._web_driver.save_screenshot(file_name)
#
#     def scroll_down(self, offset=0):
#         """ Scroll the page down. """
#
#         if offset:
#             self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
#         else:
#             self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#
#     def scroll_up(self, offset=0):
#         """ Scroll the page up. """
#
#         if offset:
#             self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
#         else:
#             self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')
#
#     def switch_to_iframe(self, iframe):
#         """ Switch to iframe by it's name. """
#
#         self._web_driver.switch_to.frame(iframe)
#
#     def switch_out_iframe(self):
#         """ Cancel iframe focus. """
#         self._web_driver.switch_to.default_content()
#
#     def get_current_url(self):
#         """ Returns current browser URL. """
#
#         return self._web_driver.current_url
#
#     def get_page_source(self):
#         """ Returns current page body. """
#
#         source = ''
#         try:
#             source = self._web_driver.page_source
#         except:
#             print(colored('Con not get page source', 'red'))
#
#         return source
#
#     def check_js_errors(self, ignore_list=None):
#         """ This function checks JS errors on the page. """
#
#         ignore_list = ignore_list or []
#
#         logs = self._web_driver.get_log('browser')
#         for log_message in logs:
#             if log_message['level'] != 'WARNING':
#                 ignore = False
#                 for issue in ignore_list:
#                     if issue in log_message['message']:
#                         ignore = True
#                         break
#
#                 assert ignore, 'JS error "{0}" on the page!'.format(log_message)
#
#     def wait_page_loaded(self, timeout=60, check_js_complete=True,
#                          check_page_changes=True, check_images=False,
#                          wait_for_element=None,
#                          wait_for_xpath_to_disappear='',
#                          sleep_time=2):
#         """ This function waits until the page will be completely loaded.
#             We use many different ways to detect is page loaded or not:
#
#             1) Check JS status
#             2) Check modification in source code of the page
#             3) Check that all images uploaded completely
#                (Note: this check is disabled by default)
#             4) Check that expected elements presented on the page
#         """
#
#         page_loaded = False
#         double_check = False
#         k = 0
#
#         if sleep_time:
#             time.sleep(sleep_time)
#
#         # Get source code of the page to track changes in HTML:
#         source = ''
#         try:
#             source = self._web_driver.page_source
#         except:
#             pass
#
#         # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
#         while not page_loaded:
#             time.sleep(0.5)
#             k += 1
#
#             if check_js_complete:
#                 # Scroll down and wait when page will be loaded:
#                 try:
#                     self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#                     page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
#                 except:
#                     pass
#
#             if page_loaded and check_page_changes:
#                 # Check if the page source was changed
#                 new_source = ''
#                 try:
#                     new_source = self._web_driver.page_source
#                 except:
#                     pass
#
#                 page_loaded = new_source == source
#                 source = new_source
#
#             # Wait when some element will disappear:
#             if page_loaded and wait_for_xpath_to_disappear:
#                 bad_element = None
#
#                 try:
#                     bad_element = WebDriverWait(self._web_driver, 0.1).until(
#                         EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
#                     )
#                 except:
#                     pass  # Ignore timeout errors
#
#                 page_loaded = not bad_element
#
#             if page_loaded and wait_for_element:
#                 try:
#                     page_loaded = WebDriverWait(self._web_driver, 0.1).until(
#                         EC.element_to_be_clickable(wait_for_element._locator)
#                     )
#                 except:
#                     pass  # Ignore timeout errors
#
#             assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)
#
#             # Check two times that page completely loaded:
#             if page_loaded and not double_check:
#                 page_loaded = False
#                 double_check = True
#
#         # Go up:
#         self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

#####################################
from selenium.webdriver.support.wait import WebDriverWait


class WebPage(object):
    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self._url = url

    def open(self):
        self._web_driver.get(self._url)

    def find_element(self, locator):
        return self._web_driver.find_element(*locator)

    def find_elements(self, locator):
        return self._web_driver.find_elements(*locator)

    @property
    def current_url(self):
        return self._web_driver.current_url
#######################################
'''TO DO - implement locators in separate class'''
# class MainPageLocator():
#     class MainPageLocator():
#         menu_home = WebElement(By.XPATH, '//a[text()="Home"]')
#         contacts_head = WebElement(By.XPATH, '//h2')
#         sign_in_button = WebElement(By.XPATH, '//button[text()="Sign In"]')
#         sign_up_button = WebElement(By.XPATH, '//button[text()="Sign Up"]')

class HomePage(WebPage):
    # Локатори елементів сторінки
    menu_home =                         (By.XPATH,'//a[text()="Home"]')
    about_btn_locator =                 (By.XPATH,'//button[text()="About"]')
    contacts_head =                     (By.XPATH,'//h2')
    '''Login modal window locators'''
    sign_in_button =                    (By.XPATH,'//button[text()="Sign In"]')
    sign_up_button =                    (By.XPATH,'//button[text()="Sign Up"]')
    modal_title_login =                 (By.XPATH,'//h4[text()="Log in"]')
    email_input =                       (By.NAME,"email")
    pswd_input =                        (By.ID,"signinPassword")
    remember_me_chekbx =                (By.ID,"remember")
    forgot_pass_btn =                   (By.XPATH,'//button[text()="Forgot password"]')
    registration_btn =                  (By.XPATH,'//button[text()="Registration"]')
    login_btn =                         (By.XPATH,'//button[text()="Login"]')
    wrong_log_pass_allect_loctr =       (By.XPATH, '//p[text()="Wrong email or password"]')
    '''After signin locators'''
    garage_text_loctr =                 (By.XPATH,'// h1[text() = "Garage"]')


    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

        # Додайте методи для доступу до елементів сторінки, якщо необхідно:
    def click_home_menu(self):
        self.find_element(self.menu_home).click()

    def get_contacts_header_text(self):
        return self.find
            # find_element(self.contacts_head).text

    def click_sign_in_button(self):
        self.find_element(self.sign_in_button).click()

    def wait_for_modal_login_to_appear(self):
        wait = WebDriverWait(self._web_driver, 30)
        wait.until(EC.presence_of_element_located(self.modal_title_login))

    def click_sign_up_button(self):
        self.find_element(self.sign_up_button).click()

    def enter_email(self, email):
        email_input = self.find_element(self.email_input)
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.find_element(self.pswd_input)
        password_input.send_keys(password)

    def click_login_button(self):
        login_btn = self.find_element(self.login_btn)
        login_btn.click()

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False
