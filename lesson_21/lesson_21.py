from pony.orm import *
from pony.orm.core import sql_logger

db = Database()

mysql = dict(provider='mysql',
             host="https://databases.000webhost.com/index.php?route=/database/structure&db=id18337469_person",
             user="user",
             passwd="asdQWE!@#123",
             db='person')

sqlite = dict(provider='sqlite',
              filename='person.db',
              create_db=True)


class Person(db.Entity):
    name = Required(str)
    age = Optional(int)
    cars = Set('Car')


class Car(db.Entity):
    make = Required(str)
    model = Optional(str)
    owner = Required(Person)

db.bind(sqlite)
db.generate_mapping(create_tables=True)
set_sql_debug(True)
# @db_session
# def add_user():
#     p1 = Person(name='Isaak', age=45)
#     c1 = Car(make="Audi", model="fdfd", owner=p1)
#     db.commit()
# add_user()
@db_session
def output():
    # print(Car.select().show())
    # print(Person.select().show())
    result = select(p for p in Person if p.age <= 20)
    for r in result:
        print(r)
output()
