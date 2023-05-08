# import requests
# r = requests.api
# TypeError
# "1" + 1
# IndexError
# a = [1,2]
# a[4]
# ZeroDivisionError
# 1/0
# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
# except ValueError:
#     print("Invalid input. Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Result is:", y)

def input_number():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
    except (ValueError, ZeroDivisionError):
        print("its not a number or Cannot divide by zero")
        return input_number()
    return x, y

x,y = input_number()
print(x, y)