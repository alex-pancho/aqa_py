import pytest
import logging


log  = logging.getLogger(__name__)


class DBConnection():
    count = 0

    def __init__(self) -> None:
        self.__class__.count = self.count + 1
        self.connection = "You connect to Pentagon DB"

    def __repr__(self) -> str:
        return f"{self.connection} {self.count}"


@pytest.fixture()  # autouse=True   # scope="module"
def connect_to_database():
    connection = DBConnection()
    # assert connection == 0  ## ERROR
    return connection


def test_connect(connect_to_database):
    assert isinstance(connect_to_database, DBConnection), connect_to_database  ## FAILS
    log.info(connect_to_database)
    assert connect_to_database.connection == "You connect to Pentagon DB", connect_to_database.connection


def test_connect_2(connect_to_database):
    assert isinstance(connect_to_database, DBConnection), connect_to_database
    log.info(connect_to_database)
    assert connect_to_database.connection == "You connect to Pentagon DB", connect_to_database.connection
