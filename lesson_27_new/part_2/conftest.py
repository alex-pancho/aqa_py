import get_browser
import pytest

URL = "https://guest:welcome2qauto@qauto.forstudy.space/"

@pytest.fixture(scope="module")
def driver():
    _driver = get_browser.firefox(True)
    _driver.get(URL)
    yield _driver
    _driver.quit()