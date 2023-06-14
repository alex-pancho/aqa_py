import abc

class Parent(abc.ABC):
    @abc.abstractmethod
    def get_info(self, parameter):
        """Get parameter info"""
    @abc.abstractmethod
    def set_info(self, parameter, value):
        """Set parameter to value"""

class Child(Parent):
    def __init__(self) -> None:
        self._parmeter = {}

    def get_info(self, key):
        return self._parmeter.get(key)

    def set_info(self, key, value):
        self._parmeter[key] = value
        return self._parmeter

# p1 = Child()
# print(p1.set_info("a", 1))
# print(p1.get_info("a"))

i = iter("abc")
print(next(i))
print(next(i))
print(next(i))
# print(next(i))  ## StopIteration

def my_for(iterable, callback_func):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
            callback_func(value)
        except StopIteration:
            break

def loop_print(value):
    print(value)

my_for('bye', loop_print)
ab = list("abdfdfd")
print(ab)
cd = list({1:"aa", 2:"bb", 3:"cc"})
print(cd)

def gen():
    yield "Hello"
    yield "world"

g = gen()
print(next(g))
print(next(g))

def count_out(max_cnt):
    count = 1
    while count <= max_cnt:
        yield count
        count +=1

for i in count_out(5):
    print(i)
