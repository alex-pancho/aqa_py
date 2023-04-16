# task 01 == Розділіть змінну так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
alice_in_wonderland = "Would you tell me, please, which way I ought to go from here?" \
    "That depends a good deal on where you want to get to, said the Cat." \
    "I don\'t much care where - said Alice." \
    "Then it doesn't matter which way you go, said the Cat." \
    "- so long as I get somewhere,Alice added as an explanation." \
    "Oh, you\'re sure to do that, said the Cat, if you only walk long enough."
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("# task 03:", alice_in_wonderland)

"""
# task 04
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_space = 436402 #км2
azov_sea_space = 37800 #км2
s_of_black_and_azov_sea = black_sea_space + azov_sea_space
print("# task 04: Чорне та Азовське моря разом займають", s_of_black_and_azov_sea, "км2")

"""
# task 05
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_of_3_supermarkets = 375291 #products
sum_of_1_and_2_supermarkets = 250449 #products
sum_of_2_and_3_supermarkets = 222950 #products

products_3_supermarket = sum_of_3_supermarkets - sum_of_1_and_2_supermarkets
products_1_supermarket = sum_of_3_supermarkets - sum_of_2_and_3_supermarkets
products_2_supermarket = sum_of_3_supermarkets - products_3_supermarket - products_1_supermarket

print("# task 05: В першому супермаркетi розміщено", products_1_supermarket, "товару,",
      "в другому", products_2_supermarket, "товару,",
      "в третьому", products_3_supermarket, "товару.")
"""
# task 06
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month_payment = 1179 #Hrn
one_year = 12 #Month
half_year = one_year / 2
one_and_half_year = one_year + half_year #Totalmonth
total_comp_price = one_month_payment * one_and_half_year
print("# task 06: Вартість комп’ютера становить:", total_comp_price, "грн")
"""
# task 07
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("# task 07:" "\nОстача від діленя чисел:"\
     "\na)",a, "", "d)", d,
     "\nb)",b, "", "e)", e,
     "\nc)",c, "", "f)", f)
"""
# task 08
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274 #hrn
medium_pizza = 218 #hrn
juce = 35 #hrn
cake = 350 #hrn
water = 21 #hrn

big_pizza_x4 = big_pizza * 4
medium_pizza_x2 = medium_pizza * 2
juce_x4 = juce * 4
water_x3 = water * 3
total_bd_price = big_pizza_x4 + medium_pizza_x2 + juce_x4 + water_x3 + cake

print("# task 08: Вартість кожного замовлення:",
      "\n1) Чотири великих піци:", big_pizza_x4, "грн"
      "\n2) Дві середні піци:", medium_pizza_x2, "грн"
      "\n3) Чотири пляшки сіку:", juce_x4, "грн"
      "\n4) Три пляшки води:", water_x3, "грн"
      "\n5) Торт:",cake,"грн"
      "\nВсього було витрачено:", total_bd_price, "грн")
"""
task 09:
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232 #quantity
one_page_photos = 8 #quantity of photo on one album page
total_pages_need = total_photo / one_page_photos
print("# task 09: Ігорю знадобиться", round(total_pages_need), "сторiнок.")

"""
# task 10
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
import math
total_range = 1600 #km
consumption_per_100km = 9 #liters
total_tank_space = 48 #liters
total_fuel_consumption = total_range / 100 * 9 #liters
number_of_filling = total_range / total_tank_space
print("# task 10:""\n1) Для такої подорожі знадобиться", round(total_fuel_consumption), "лiтри бензину",
      "\n2) Кількість заправок до повного баку", math.ceil(number_of_filling)) #округлив до бiльшого значення

adwentures_of_tom_sawer = """2222 2222 dgdsgfdgd wetetertert  rfegergergtergergrge  regergrgr """

q1 = adwentures_of_tom_sawer.split(".")
count = 0

for item in q1:
    if item[0].isupper():
        count += 1
print(count)












