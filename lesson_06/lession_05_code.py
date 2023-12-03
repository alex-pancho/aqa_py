# Булеві значення та порівняння
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')


False # "", {}, [], (), 0

# оператор if
age =  44 #int(input("Type your age: "))
if age < 18:
    print("That is not the correct answer. Please try again!")
elif age > 43:
    print("Ok, and you have a discount")
else:
    print("Ok, can go!")
# else

# elif
age = 18 # int(input("Type your age 2: "))
# if в один рядок
#value = 1 if answer else 2
message = "Please try again!" if age < 18 else "Ok, can go!"
print(message)

# цикл while
current_number = 0
while current_number <= 4:
    current_number += 1
    if current_number == 4:
        continue
    print("while print me:", current_number)
# break
# continue

# цикл for
for i in range(2, 6):
    print(i)
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)
# for в один рядок
sum_el = [i for i in my_list if i%2 == 0]
print(sum_el)
