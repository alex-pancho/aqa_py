# task 01 == Розділіть змінну так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
alice_in_wonderland =  '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'


# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Output task 01 and 02: ", alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area, azov_sea_area = 436402, 37800
total_areas = black_sea_area + azov_sea_area
print("Total area of black and azov sea: ", total_areas, "km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods_qty = 375291
first_sec_warehouse = 250449
second_third_warehouse = 222950
first_wareh_qty_goods = total_goods_qty - second_third_warehouse
secong_wareh_qry_goods = first_sec_warehouse - first_wareh_qty_goods
third_wareh_qey_goods = second_third_warehouse - secong_wareh_qry_goods
print(" Q-ty goods in 1-st warehouse",f"{first_wareh_qty_goods}","\n","Q-ty goods in 2-st warehouse",f"{secong_wareh_qry_goods}""\n","Q-ty goods in 3-st warehouse",f"{third_wareh_qey_goods}""\n")


print("1-2 = ", total_areas-first_sec_warehouse)
print("2-3=", total_goods_qty-second_third_warehouse)
third_warehouse = None


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_half_year = 18
monthly_payment = 1179
tot_pc_cost = one_half_year * monthly_payment
print("Total PS cost after", f"{one_half_year}", "payments is",f"{tot_pc_cost}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = (8019, 8)
b = (9907, 9)
c = (2789, 5)
d = (7248, 6)
e = (7128, 5)
f = (19224, 9)

print("Module division for variable a: ", a[0] % a[1])
print("Module division for variable b: ", b[0] % b[1])
print("Module division for variable c: ", c[0] % c[1])
print("Module division for variable d: ", d[0] % d[1])
print("Module division for variable e: ", e[0] % e[1])
print("Module division for variable f: ", f[0] % f[1])

# task 08
"""
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
big_pizzas_cost = 4 * 247
middle_pizzas_cost = 2 * 218
juice_cost = 4 * 35
cake_cost = 350
water_cost = 3 * 21
total_hb_product_cost = big_pizzas_cost + middle_pizzas_cost + juice_cost + cake_cost + water_cost
print("Expected costs for Ira's BD is", total_hb_product_cost)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
one_page_photoes_qty = 8
pages = photos / one_page_photoes_qty
print("Igor is able to fill in", f"{int(pages)}", "pages")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
h_b_distance = 1600
fuel_consuming = 9
volume_fuel_tank = 48
trip_fuel_consuming = int(1600 / 100) * 9
print("Trip fuel consumprion (in liters)", trip_fuel_consuming)
print("Min q-ty gas refuel", int(trip_fuel_consuming / volume_fuel_tank))