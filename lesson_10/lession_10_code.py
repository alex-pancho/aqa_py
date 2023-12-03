from pathlib import Path
from my_logger import logger


# Як створити виключення
class InvalidInputException(Exception):
    def __init__(self, input):
        self.input = input

    def __str__(self):
        return f"Invalid input: '{self.input}' is not int"

def calculate_sum(a, b):
    if not isinstance(a, int):
        raise InvalidInputException(a)
    elif not isinstance(b, int):
        raise InvalidInputException(b)
    # ValueError - тут краще
    return a + b

#print(calculate_sum(1, "ccccc"))

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.error('Attempted to divide by zero')
        raise e
    else:
        logger.info(f'{x} divided by {y} is {result}')
        return result
    finally:
        logger.debug("final countdown")
#print(divide(5, 0))
# Створення логеру


# Строгі твердження
filename = Path("text.txt")
#assert filename.exists(), f"{filename} not found"
print("Hello!!!")
# Контекстні менеджери
# f = open(filename, 'r')
# f.write("ta ta ta")
# f.close()
## WRONG WAY!!!
# f = open(filename, 'w')
# try:
#     f.write("ta ta ta")
# finally:
#     f.close()
## GOOOD WAY::::
with open(filename, 'w') as f:
    f.write("ta ta ta")
print("end record")
