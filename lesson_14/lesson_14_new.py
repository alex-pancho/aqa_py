

class Money():
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __str__(self):
        return f"{self.amount:.2f} item(s)"

    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount + other.amount)
        elif isinstance (other, (int, float)):
            return type(self)(self.amount + other)
        else:
            raise ValueError("Неправильний тип для операції додавання")

    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount - other.amount)
        elif isinstance (other, (int, float)):
            return type(self)(self.amount - other)
        else:
            raise ValueError("Неправильний тип для операції віднімання")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return type(self)(self.amount * scalar)
        else:
            raise ValueError("Неправильний тип для операції множення")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return type(self)(self.amount / scalar)
        else:
            raise ValueError("Неправильний тип або ділення на нуль")


class UAH(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def __str__(self):
        return f"{self.amount:.2f} грн"


class USD(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def __str__(self):
        return f"${self.amount:.2f}"


class ForEx:
    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell

    def convert_to_usd(self, uah_amount):
        if isinstance(uah_amount, UAH):
            usd_amount = uah_amount.amount / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

    def convert_to_uah(self, usd_amount):
        if isinstance(usd_amount, USD):
            uah_amount = usd_amount.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

if __name__ == "__main__":

    my_hrn_cash = UAH(3757)
    print(my_hrn_cash)
    print(my_hrn_cash + UAH(25))
    print(my_hrn_cash + 100)

    my_usd_cash = USD(100)
    print(my_usd_cash)

    privatbank = ForEx(37.05, 37.57)
    pb_to_uah = privatbank.convert_to_uah(my_usd_cash)
    pb_to_usd = privatbank.convert_to_usd(my_hrn_cash)

    try:
        my_hrn_cash + my_usd_cash
    except ValueError:
        print("Wrong type for add, first exchange currency")
        my_new_cash = my_hrn_cash + pb_to_uah
        print("You can get here new cash:", my_new_cash)
    akordbank = ForEx(37.37, 38.00)
    ak_to_uah = akordbank.convert_to_uah(my_usd_cash)
    ak_to_usd = akordbank.convert_to_usd(my_hrn_cash)
    print(f"Продати {my_usd_cash}:", pb_to_uah, "|", ak_to_uah)
    print(f"Купити на {my_hrn_cash}:", pb_to_usd, "|", ak_to_usd)

    for_bussiness = UAH(500)
    after_startup = for_bussiness * 3
    print(after_startup)
