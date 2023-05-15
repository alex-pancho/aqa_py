class Operation:

    balance = 0

    def add(self, sum):
        self.balance += sum

    def withdraw(self,sum):
        self.balance -= sum    


class Account(Operation): #Account will inherit everything from class Operation
    """Its defaul account class"""

#functions = methods built in class
#init is used, so class cannot be made without needed attributes
    def __init__(self, name:str, balance:float) -> None:
        self.name = name
        self.balance = balance
    def __repr__(self) -> str:
        return f"Currency:{self.name}, Balance:{self.balance}"
    
    bank = "YourBank"

# class Date:

#     formats = {
#     'ymd' : '{d.year}-{d.month}-{d.day}',
#     'mdy' : '{d.month}/{d.day}/{d.year}',
#     'dmy' : '{d.day}/{d.month}/{d.year}'
#     }

#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = self.formats[code]
#         return fmt.format(d=self)

# d = Date(2012, 12, 21)
# # print(format(d))
# # print(format(d, 'mdy'))
# #print(format(d, 'dym')) # error, n/a format

# class BlockedAccount(Operation):

#     def __init__(self, name:str, balance:float) -> None:
#         self.name = name
#         self.balance = balance

#     def add(self, sum):
#         pass

#     def __s__(self):
#         return 5

# rub_acc = BlockedAccount("rub", 1)
# rub_acc.add(1)
# #print(rub_acc.__s__())



usd_account = Account("usd", 10000)
print(usd_account.name, usd_account.balance, usd_account.bank)

grn_account = Account("grn", 1000)
print(grn_account)

grn_account.add(500)
print(grn_account.balance)

grn_account.withdraw(1200)
print(grn_account.balance)


