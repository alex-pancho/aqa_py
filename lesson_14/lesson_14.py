class Adress:
    """some docs"""
    n = 5
    # @staticmethod
    # def add(value):
    #     return value + Adress.n
    def add(self, value):
        return value + self.n

a = Adress()
a.n = 2
print("a.n", a.n)
print(a.add(2))
b = Adress()
print("b.n", b.n)
#b.foo AttributeError: 'Adress' object has no attribute 'foo'

class Terminator:

    def __init__(self, age:int) -> None:
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age:int):
        if not isinstance(age, int):
            raise ValueError("Age must be int")
        self.__age = age

t1 = Terminator(1)
#print(t1._Terminator__age) # доступ до прихов. атриб
print(t1.age)
t1.age = 2
print(t1.age)

class T:
    CELSIUS = 1
    FAHRENHEIT = 2
    def __init__(self, t, scale=CELSIUS):
        if scale == T.CELSIUS:
            self.c = t
        else:
            self.f = t

    @property
    def f(self):
        return (self.c * 9/5) + 32

    @f.setter
    def f(self, f):
        self.c = (5/9) * (f - 32)

    def __str__(self):
        return str(self.c) + '°C'

human_body = T(36.6)
print(human_body)
print(human_body.f)
t1 = T(32, T.FAHRENHEIT)
print(t1)

#uspadkuvannya

class Street(Adress):
    pass

print(issubclass(Street, Street))
print(issubclass(Adress, Adress))
print(Street.__base__.__base__) # батьки
print(dir(Street))
print(Adress.__dict__)