# create first class
class Bank:
    bank = "UtorBANK"

class Operation(Bank):
    balance = 0
    def add(self, sum):
        """Add money to acc"""
        self.balance += sum

    def withdraw(self, sum):
        self.balance -= sum

class Account(Operation):
    """Its default account class"""

    def __init__(self, name:str, balance:float) -> None:
        self.name = name
        self.balance = balance

    def __repr__(self) -> str:
        return f"Валюта:{self.name}, Баланс: {self.balance}"


# grn_acc = Account("grn", 1000)
# print(grn_acc.name, grn_acc.balance)
# print("bank", grn_acc.bank)
# usd_acc = Account("usd", 10000)
# print(usd_acc.name, usd_acc.balance)
# print("bank", usd_acc.bank)
# grn_acc.add(1000)
# grn_acc.withdraw(50)
# print(grn_acc.balance)
# grn_acc.bank = "U2Bank"

# rub_acc = Account()  # error TypeError: Account.__init__() missing 2 required positional arguments
#print(grn_acc)



class Date:
    formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = self.formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 21)
print(format(d))
print(format(d, 'mdy'))
# print(format(d, 'dym')) # n/a format type


class BlockedAccount(Operation):

    def __init__(self, name:str, balance:float) -> None:
        self.name = name
        self.balance = balance

    def add(self, sum):
        pass

    def __s__(self):
        return 5

rub_acc = BlockedAccount("rub", 1)
rub_acc.add(1)
print(rub_acc.__s__())

