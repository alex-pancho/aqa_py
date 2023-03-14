# task 01 == Виправте синтаксичні помилки
print("Hello world!", end = " ")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
   print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
x = 0 #Олександре, навіщо ця змінна?

# # task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
x = apples * 4
banana = x
print(banana)

#
# task 05 == виправте назви змінних
storona = 1
storona_2 = 2
сторона_3 = 3
__orona_4 = 4
print("Variables:", f"{storona}, {storona_2}, {сторона_3}, {__orona_4}")

# # task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = x + x + x + x
perimetery_alter_var = storona+storona_2+сторона_3+__orona_4
print("Perimetr:", perimetery_alter_var)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
grusha_trees = apple_trees + 5
sliva_trees = apple_trees - 2

print("Total trees q-ty:", apple_trees+grusha_trees+sliva_trees)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# init_temperature = 0
dinner_time = 12
before_din_time_temp = 5
after_dinn_time_temp = 10
nadvech_temp = 4

total_temp = before_din_time_temp - after_dinn_time_temp + nadvech_temp
print("Total temp: " f"{total_temp}" "°C")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
