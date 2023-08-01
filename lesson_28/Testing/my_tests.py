from project_utils import do_auth_to_forstudy

# Отримуємо авторизовану сторінку для тестування головної сторінки


def test_main_page():
    driver = do_auth_to_forstudy()
    print(driver)
    window = do_auth_to_forstudy()
    assert window
