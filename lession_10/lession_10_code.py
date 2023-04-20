from pathlib import Path
from my_logger import logger


# Як створити виключення
class InvalidInputException(Exception):
    def __init__(self, input):
        self.input = input

    def __str__(self):
        return f"Invalid input: {self.input}"

def calculate_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise InvalidInputException(f"{a} or {b}")
    return a + b

#print(calculate_sum(1, "a"))

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.error('Attempted to divide by zero')
        raise e
    else:
        logger.info(f'{x} divided by {y} is {result}')
        return result

# Строгі твердження
filename = Path("file.txt")
#assert filename.exists(), f"{filename} not found"


# f = open(filename, 'w')
# try:
#     f.write("ta ta ta")
# finally:
#     f.close()
# # Контекстні менеджери
# with open(filename, 'w') as f:
#     f.write("ta ta ta")



if __name__ == '__main__':
    divide(10, 5)
    divide(10, 0)