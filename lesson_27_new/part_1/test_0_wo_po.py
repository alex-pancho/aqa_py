from get_browser import firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Login(unittest.TestCase):

    def test_login(self):
        # Ініціалізація драйвера Chrome
        driver = firefox()
        driver.get("https://semantic-ui.com/examples/login.html")  # Замініть URL на свій

        # Заповнення даними для входу на сторінку авторизації
        driver.find_element(
            By.NAME,
            "email").send_keys("user@gmail.com")
        driver.find_element(
            By.NAME,
            "password").send_keys("my supersecret password")
        driver.find_element(
            By.XPATH,
            '//form//div[.="Login"]').click()

        # Перевірка, що тег h1 містить текст "Hello userName" після авторизації
        h1_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2")))
        self.assertTrue(h1_element.is_displayed())
        self.assertEqual(h1_element.text, "Log-in to your account")

        # Закриття браузера
        driver.quit()

if __name__ == "__main__":
    unittest.main()

"""
Цей підхід має дві проблеми.

    Немає поділу між методом тестування і локаторами AUT
    (ідентифікаторами в цьому прикладі);
    обидва переплетені в одному методі.
    Якщо в інтерфейсі користувача AUT змінюються ідентифікатори,
    макет або спосіб введення та обробки логіну, повинен змінитися
    і сам тест.
    Ідентифікатори-локатори будуть розподілені в декількох тестах,
    у всіх тестах, які мають використовувати цю сторінку входу в систему.

Застосовуючи техніку page object, цей приклад можна
 переписати так, як показано в наступному прикладі:
  page object для сторінки входу в систему.
"""