import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from lesson_27_new.part_2.src.pages.home_page import HomePage as HP

def test_homepage(driver):
    page = HP(driver)