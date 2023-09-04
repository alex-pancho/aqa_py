from hillel_api import *
import pytest
from ideas_for_test.sql_client.sqlite3_client import SQLiteClient
from conftest import TEST_DB_URL
import ideas_for_test.schemas.auth_schema as auth_schema
import ideas_for_test.schemas.users_schema as users_schema
from ideas_for_test.validators.validators import Response

usr_id = None  # За це пояснюю нижче


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", [
    ("Giga", "Chad", "gachiboy715@gmail.com", "WE7865kulv67", "WE7865kulv67"),
    ("Johan", "Dvir", "dontmisswithjohannqv@gmail.com", "777heRo777", "777heRo777")])
def test_signup_positive(name, last_name, email, password, repeat_password, read_users_from_database_function, clean_database):
    global usr_id
    command = """
        INSERT INTO users (user_id, email, password) VALUES (?, ?, ?);
        """

    user_data = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }

    # Відправляємо запит
    r = auth.signup(s, user_data)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic і беремо
    # json відповіді в успішному випадку
    response = Response(r)
    response.assert_status_code(201).validate(auth_schema.Post)
    r_json = response.response_json

    # Перевіряємо чи запишеться юзер у базу даних
    user_id = r_json["data"]["userId"]
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    client.execute_command(command, (user_id, email, password))
    usrs = read_users_from_database_function()
    assert len(usrs) == 1, "User not in table"
    user = usrs[0]
    assert user[0] == user_id, "Not user_id parameter in table"
    assert user[1] == email, "Not email parameter in table"
    assert user[2] == password, "Not password parameter in table"
    usr_id = user_id


# Цей запит залежний від того чи авторизований юзер, тому спочатку треба виконувати тест з валідною авторизацією чи
# вставляти у цей тест також авторизацію, навіть не знаю, що гірше але я обрав перший варіант)
def test_current_positive(read_users_from_database_function):
    # Робимо запит
    r = users.current(s)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic
    response = Response(r)
    response.assert_status_code(200).validate(users_schema.GetCurrent)

    # Перевіряємо за айдішником, що маємо справу саме з останнім залогіненим юзером
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    usrs = read_users_from_database_function()
    assert len(usrs) == 1
    user = usrs[0]
    assert user[0] == usr_id


# Цей також
def test_profile_get_positive(read_users_from_database_function):
    # Робимо запит
    r = users.profile_get(s)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic
    response = Response(r)
    response.assert_status_code(200).validate(users_schema.GetProfile)

    # Перевіряємо за айдішником, що маємо справу саме з останнім залогіненим юзером
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    usrs = read_users_from_database_function()
    assert len(usrs) == 1
    user = usrs[0]
    assert user[0] == usr_id


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", [
    ("John", "Down", "wrong@test@.com", "qwerty123", "qwerty123"),  # невалідний емейл
    ("John", "Down", "wron.g@test.com", "qwerty123", "qwerty123"),
    ("John", "Down", "wrongtest.com", "qwerty123", "qwerty123"),
    ("John", "Down", "wrong@test.com.ua", "qwerty123", "qwerty123"),
    ("John", "Down", "goodmilo777@gmail.com", "12345", "12345"),  # невалідний пароль
    ("John", "Down", "goodmilo777@gmail.com", "      ", "      "),
    ("John", "Down", "goodmilo777@gmail.com", "NormParol777", "WrongParol777"),
    ("", "", "goodmilo777@gmail.com", "NormParol777", "NormParol777")])  # невлідне ім'я
def test_signup_negative(name, last_name, email, password, repeat_password, read_users_from_database_function, clean_database):
    command = """
        INSERT INTO users (user_id, email, password) VALUES (?, ?, ?);
        """

    user_data = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }

    # Відправляємо запит
    r = auth.signup(s, user_data)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic і беремо
    # json відповіді в успішному випадку
    response = Response(r)
    response.assert_status_code(400).validate(auth_schema.Error)
    r_json = response.response_json

    # Перевіряємо, що БД пуста
    try:
        user_id = r_json["data"]["userId"]
    except KeyError:
        pass
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    try:
        client.execute_command(command, (user_id, email, password))
    except UnboundLocalError:
        pass
    usrs = read_users_from_database_function()
    assert len(usrs) == 0, "Table is not empty!"


@pytest.mark.parametrize("email, password, remember", [("dontmisswithjohannqc@gmail.com", "777heRo777", False),
                                                       ("gachiboy750@gmail.com", "WE7865kulv67", True)])
def test_sigin_positive(email, password, remember):

    user_data = {
        "email": email,
        "password": password,
        "remember": remember
    }

    # Відправляємо запит
    r = auth.signin(s, user_data)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic
    response = Response(r)
    response.assert_status_code(200).validate(auth_schema.Post)


@pytest.mark.parametrize("email, password, remember", [("qam@2022test.com", "Qam2", False),
                                                       ("qam@2022test.com", "Qam2", "Yes")])
def test_sigin_negative(email, password, remember):

    user_data_negative = {
        "email": email,
        "password": password,
        "remember": remember
    }

    r = auth.signin(s, user_data_negative)
    response = Response(r)
    response.assert_status_code(400).validate(auth_schema.Error)


def test_logout():
    r = auth.logout(s)
    response = Response(r)
    response.assert_status_code(200).validate(auth_schema.Get)


def test_current_negative(read_users_from_database_function):
    # Робимо запит
    r = users.current(s)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic
    response = Response(r)
    response.assert_status_code(401).validate(users_schema.Error)

    # Перевіряємо, що у базі нема юзерів
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    usrs = read_users_from_database_function()
    assert len(usrs) == 0


def test_profile_get_negative(read_users_from_database_function):
    # Робимо запит
    r = users.profile_get(s)

    # Валідуємо, що нам прийшов необхідний статус та прийшли необхідні за вимогами поля за допомогою pydentic
    response = Response(r)
    response.assert_status_code(401).validate(users_schema.Error)

    # Перевіряємо, що у базі нема юзерів
    client = SQLiteClient(TEST_DB_URL)
    client.create_conn()
    usrs = read_users_from_database_function()
    assert len(usrs) == 0
