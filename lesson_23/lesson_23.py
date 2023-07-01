import requests
import time


def decorator_function(func):
    def wrapper():
        print('Обгортка!')
        print('Ми виконуємо: {}'.format(func))
        print('Отож...')
        func()
        print('Вихід')
    return wrapper


@decorator_function
def run():
    print("Its run")


# run()

# def benchmark(func):

#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Час виконання: {} секунд.'.format(end-start))
#         return return_value
#     return wrapper


# @benchmark
# def fetch_webpage(url):
#     webpage = requests.get(url)
#     return webpage.status_code


# webpage = fetch_webpage('https://google.com')
# print(webpage)


def benchmark(iters):

    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total_current = (end-start)
                print(f'[*] Час виконання: {total_current} секунд.')
                total = total + total_current
            print(f'[*] Середній час виконання: {total/iters} секунд.')

            return return_value
        return wrapper
    return actual_decorator


@benchmark(1)
def fetch_webpage(url):
    webpage = requests.get(url)
    return webpage.status_code


webpage = fetch_webpage('https://google.com')
print(webpage)


def decor(func):
    return func("Mary")


@decor
def print_hello(name):
    print(f"Hello, {name}")


print_hello
