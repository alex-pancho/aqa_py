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