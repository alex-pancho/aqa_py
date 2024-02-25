import sys
import pathlib
root = str(pathlib.Path(__file__).parents[3])
sys.path.insert(0, root)
from lesson_27_new.part_2.src.pages.home_page import HomePage as HP

def test_homepage(driver):
    home_page = HP(driver)
    element = home_page.menu_home()
    assert element.is_visible(), f"Not found: {element._locator}"
