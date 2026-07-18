print('task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
print("task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті:'")
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for simvol in alice_in_wonderland:
    if simvol == "'":
        print(simvol)
print("task 03 == Виведіть змінну alice_in_wonderland на друк:")
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

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
print('task 04')
Black_Sea = 436402
Azov_Sea = 37800
plochad = Black_Sea+Azov_Sea
print(f'''Площадь Черного моря: {Black_Sea} км2, а Азовсткого: {Azov_Sea} км2.
Их общая пладащь равна: {Black_Sea} + {Azov_Sea} = {plochad} км2''')
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('task 05')
sklad1_2 = 250449
sklad2_3 = 222950
vsego = 375291
sklad3 = vsego - sklad1_2
sklad2 = sklad2_3 - sklad3
sklad1 = sklad1_2 - sklad2
print(f'''На первом и втором складе {sklad1_2} товаров
на втором и тертьем сладе {sklad2_3}
Всего на трех складах {vsego}''')
print(f'''Склад 3 = {vsego} - {sklad1_2} = {sklad3} шт''')
print(f'''Склад 2 = {sklad2_3} - {sklad3} = {sklad2} шт''')
print(f'''Склад 3 = {sklad1_2} - {sklad2} = {sklad1} шт''')
print(f'''Товаров на первом складе = {sklad1} шт
Товаров на втором складе = {sklad2} шт
Товаров на третьем складе = {sklad3} шт''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('task 06')
month = 18
kredit = 1179
comp= month * kredit
print(f"""Ежемесячный платеж: {kredit} грн
Срок выплаты: {month} месяцев""")
print(f'''Полная стоимость компьютера равна: {kredit} * {month} = {comp} грн''')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('task 07')

chislo = {
    "a": [8019, 8],
    "b": [9907, 9],
    "c": [2789, 5],
    "d": [7248, 6],
    "e": [7128, 5],
    "f": [19224, 9]}
print(f'''a = {chislo['a'][0]} % {chislo['a'][1]} = {chislo['a'][0] % chislo['a'][1]}''')
print(f'''b = {chislo['b'][0]} % {chislo['b'][1]} = {chislo['b'][0] % chislo['b'][1]}''')
print(f'''c = {chislo['c'][0]} % {chislo['c'][1]} = {chislo['c'][0] % chislo['c'][1]}''')
print(f'''d = {chislo['d'][0]} % {chislo['d'][1]} = {chislo['d'][0] % chislo['d'][1]}''')
print(f'''e = {chislo['e'][0]} % {chislo['e'][1]} = {chislo['e'][0] % chislo['e'][1]}''')
print(f'''f = {chislo['f'][0]} % {chislo['f'][1]} = {chislo['f'][0] % chislo['f'][1]}''')

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

print('task 08')
pokupki = {"Піца велика": [4, 274], "Піца середня": [2, 218], "Сік": [4, 35], "Торт": [1, 350], "Вода": [3, 21],}
pizza_big = pokupki["Піца велика"][0] * pokupki["Піца велика"][1]
pizza_mid = pokupki["Піца середня"][0] * pokupki["Піца середня"][1]
sik= pokupki["Сік"][0] * pokupki["Сік"][1]
tort= pokupki["Торт"][0] * pokupki["Торт"][1]
voda= pokupki["Вода"][0] * pokupki["Вода"][1]
print(f"""Пиццы большие = {pizza_big} грн
Пиццы средние = {pizza_mid} грн
Соки = {sik} грн
Торты = {tort} грн
Вода = {voda} грн""")
print(f"Ире нужно всего {pizza_big+pizza_mid+sik+tort+voda} денег")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

print('task 09')
vsego_foto = 232
stranica = 8
albom = vsego_foto / stranica
print(int(albom))
print(f"""Всего фотографий = {vsego_foto} шт
Фотографий на одной странице = {stranica} шт""")
print(f'''Количество страниц в альбоме: {vsego_foto} / {stranica} = {int(albom)} страниц''')

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

print('task 10')
Kh_Bud = 1600
razhod = 9
bak = 48
print(f"""Расстояние Харьков - Будапешт = {Kh_Bud} км
Расход бензина = {razhod} л на 100 км
Вместимость бака = {bak} л""")
vsego_litrov = (Kh_Bud/100) * razhod
print(f'''1) Всего бензина на поездку: ({Kh_Bud} / 100) * {razhod} = {int(vsego_litrov)} литров''')
kol_zapravok= vsego_litrov / bak
print(f'''2) Заездов на заправку в пути: ({int(vsego_litrov)} - {bak}) / {bak} = {int(kol_zapravok)} раза''')