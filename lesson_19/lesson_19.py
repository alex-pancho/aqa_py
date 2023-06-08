import sqlite3
connection = None


class DB_one():

    def __init__(self, filename) -> None:
        self.conn_to_db(filename)

    def conn_to_db(self, filename):
        self.connection = sqlite3.connect(filename) # ':memory:'
        self.cur = self.connection.cursor()


cur = DB_one("lesson_19.db")


def conn_to_db():
    global connection
    connection = sqlite3.connect(':memory:')
    cur = connection.cursor()
    return cur


def create_table(cur, name="users"):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {name}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name,
        gender  INTGER,
        hobbies,
        street,
        area,
        landmark,
        province,
        city,
        zip
        );''')
    connection.commit()


def insert_data(cur, csv):
    cur.execute(f"INSERT INTO users (first_name, last_name) VALUES {csv}")
    connection.commit()


def select_data(cur, select):
    return cur.execute(select).fetchall()


cur = conn_to_db()

create_table(cur)

csv = "('David', 'Solomonovich')"
csv2 = "('Ivan', 'Pobivan')"
insert_data(cur, csv)
insert_data(cur, csv2)
data = select_data(cur, 'SELECT * FROM users;')
print(data)

connection.close()
# .fetchmany(3) - три перші результати, далі наступні