from get_browser import firefox
from first_page_object import SignInPage


URL = "https://semantic-ui.com/examples/login.html"


def test_login():
    driver = firefox()
    sign_in = SignInPage(driver, URL)
    assert sign_in.driver is not None
    user = "user@gmail.com"
    password = "my supersecret password"

    afrer_login = sign_in.login_valid_user(user, password)
    assert afrer_login.get_message_text() == "Log-in to your account"