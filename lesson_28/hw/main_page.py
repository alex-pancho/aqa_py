from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_signin_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, ".btn.header_signin")
        login_link.click()

    def should_be_signin_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, '.btn.header_signin'), "Sign in link is not presented"

    def should_be_navbar_links(self):
        for i in range(1, 4):
            assert self.is_element_present(By.CSS_SELECTOR, f'.btn.header-link:nth-child({i})'), "Link in navbar is \
            not presented"

    def should_be_contacts_footer(self):
        assert self.is_element_present(By.XPATH, '//h2 [text()="Contacts"]')
        for i in range(1, 6):
            assert self.is_element_present(By.CSS_SELECTOR, f'div .socials_link:nth-child({i})'), "No contacts info"

    def play_video(self):
        self.get_element(By.CSS_SELECTOR, 'iframe.hero-video_frame').click()

    def guest_login(self):
        self.get_element(By.CSS_SELECTOR, 'button.-guest').click()