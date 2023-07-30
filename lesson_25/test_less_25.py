from lesson_25 import get_python, search_field, input_to
from lesson_25 import found_results, get_hillel_test
import time


def test_search():
    window = get_python()
    elem2 = search_field(window)
    input_to(elem2, "python")
    time.sleep(1)
    element = found_results(window)
    assert "No results found" not in element.text


def test_hillel():
    window = get_hillel_test()
    assert window
