import sqlite3
import pytest
import pathlib

TEST_DB_URL = pathlib.Path(__file__).parent / "test_users.db"


@pytest.fixture(scope="session", autouse=True)
def create_moderate_tables(db_connection):
    """Фікстура для створення і видалення таблиць"""
    create_user_table_query = """
CREATE TABLE IF NOT EXISTS users (
user_id serial NOT NULL,
email varchar NOT NULL,
password varchar NOT NULL
);
"""

    drop_user_table_query = """
DROP TABLE users;
"""
    db_connection.execute(create_user_table_query)  # Створюємо таблицю на початку прогону тестів
    db_connection.commit()
    yield
    db_connection.execute(drop_user_table_query)    # Видаляємо таблицю після прогону тестів
    db_connection.commit()


@pytest.fixture(scope="session")  # буде викликана 1 раз за весь час прогону тестової сесії
def db_connection():
    """Фікстура для створення з'єднання з базою"""
    return sqlite3.connect(TEST_DB_URL)


@pytest.fixture(scope="function")  # буде зачищати базу даних якщо передати її як параметр у тест
def clean_database(db_connection):  # передаємо на вхід результат роботи іншої фікстури
    """Фікстура для очищення бази від даних до прогону тесту"""
    db_connection.execute("""DELETE FROM users;""")
    db_connection.commit()


@pytest.fixture(scope="session")
def create_test_user_in_database_function(db_connection):  # фікстура використовує результат роботи іншої фікстури
    """Фікстура для створення функції для наповнення бази тестовими даними"""

    def create_user(user_id: int, email: str, password: str):
        """Функція для наповнення бази тестовими даними"""
        db_connection.execute("""INSERT INTO users (user_id, email, password) VALUES (?, ?, ?);""",
                              (user_id, email, password))
        db_connection.commit()
    return create_user


@pytest.fixture(scope="session")
def read_users_from_database_function(db_connection):  # фікстура використовує результат роботи іншої фікстури
    """Фікстура для створення функція для уточнення даних з тестової бази"""

    def read_users():
        """Функція читання з тестової бази даних"""
        cursor = db_connection.cursor()
        cursor.execute("""SELECT * FROM users;""")
        return cursor.fetchall()
    return read_users
