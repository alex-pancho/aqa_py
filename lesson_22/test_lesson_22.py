import pytest


def test_sum():
    a = 2 + 2
    b = 5
    assert a == b, f"{a} not Equal {b}"


def test_string():
    a = "more equipment while keeping a light roll. Weak in magic"
    b = "more equipment while magic a light roll. Weak in magic"
    assert a == b


def test_list():
    a = [1, 2, 3]
    b = [3, 2, 1]
    assert a == b


def test_dict():
    a = {"a": 1}
    b = {"a": 2}
    assert a == b


def get_a(a):
    return int(a)


def test_error():
    with pytest.raises(ValueError):
        a = "qwqwq"
        get_a(a)


def get_error():
    raise AttributeError("character name empty")


def test_error_message():
    with pytest.raises(
            AttributeError,
            match="character name empty"
            ):
        get_error()
