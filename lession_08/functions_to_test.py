from typing import Union


def desktop_price_define(count_month: int, month_payment: int) -> int:
    """
    Receives two positive numbers count month and month payment then
    calculates credit sum and returns result. In case when numbers not positive
    or 0 prints to user correspond message and returns None
     """
    if count_month <= 0:
        print('Count month cant\'t be 0 or less')
    elif month_payment <= 0:
        print('Month payment cant\'t be 0 or less')
    else:
        total_price = month_payment * count_month
        print(f'Total desktop price equal: {total_price} grn.')
        return total_price


def solve_igors_math_troubles(photos_all: int, max_photos_on_page: int) -> int:
    """Receives count of photos number > 0 and max count photos on page number > 0
    returns result how much pages need for all photos."""
    if photos_all % max_photos_on_page != 0:
        result = (photos_all // max_photos_on_page) + 1
        print(f'Igor needs {result} pages in his album')
        return result
    else:
        result = photos_all // max_photos_on_page
        print(f'Igor needs {result} pages in his album')
        return result


def calculate_fuel_for_trip(distance: int, tank_volume: int = 48, efforts: int = 9) -> list:
    """Receives required number arg distance and optional number tank volume, number efforts
     returns list with float and int counts where first number is count of fuels needed and second number
     count of attends gas station"""
    fuel_for_trip = (distance / 100) * efforts
    attends_gas_station = fuel_for_trip // tank_volume
    if attends_gas_station % 1 > 0:
        attends_gas_station += 1

    print(f'Family need {fuel_for_trip} litres fuel for trip and attend gas station {int(attends_gas_station)} times.')
    return [fuel_for_trip, int(attends_gas_station)]


def define_stock_goods_count(goods_all: int, first_and_second: int, second_and_third: int) -> dict:
    """Receives args all count of goods, sum of goods in first and second stocks,
    Receives args all count of goods, sum of goods in second  and third  stocks then calculates count of
    goods each stock and returns dict with name of stock and correspond count of goods"""
    stock_1 = goods_all - second_and_third
    stock_2 = first_and_second - stock_1
    stock_3 = goods_all - (stock_1 + stock_2)
    print(f'Goods in First stock: {stock_1} \nGoods in Second stock: {stock_2} \nGoods in Third stock: {stock_3}')

    return {
           "first_stock": stock_1,
           "second_stock": stock_2,
           "third_stock": stock_3
    }


def two_numbers_sum(operand_1: Union[int, float], operand_2: Union[int, float]) -> Union[int, float]:
    """ Calculates sum of two given operands"""
    return operand_1 + operand_2


def numbers_list_average(numbers_list: list) -> float:
    """ Calculates arithmetic mean from list with numbers"""
    return sum(numbers_list) / len(numbers_list)


def reversed_string(text: str) -> str:
    """Returns a reversed string from given string"""
    return text[::-1]


def squared_numbers(numbers_list: list) -> list:
    """Receives list with numbers and square even in list"""
    result = [number ** 2 for number in numbers_list if number % 2 == 0]
    return result


def find_substring(text1: str, text2: str) -> int:
    """
    Finds the lowest index in text if subtext found else returns -1 """
    return text1.find(text2)


def keys_to_values_changing(args_dict: dict) -> dict:
    """Receives dict with values and return dict where values become keys and keys become values"""
    modified_dict = {}
    for keys, values in args_dict.items():
        modified_dict[values] = keys
    return modified_dict
