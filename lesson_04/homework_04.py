adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

print(adwentures_of_tom_sawer)
##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("======================")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
#adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
#adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("======================")
print("""Виведіть, скількі разів у тексті зустрічається літера "h" """)
kol = 0
for simvol in adwentures_of_tom_sawer:
    if simvol.lower() == "h":
        kol += 1
print("""У тексті  літера "h" зустрічається""",kol,"раз")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("======================")
print("""Виведіть, скільки слів у тексті починається з Великої літери""")
kol = 0
list_slow= adwentures_of_tom_sawer.split()
for simvol in list_slow:
    if simvol.istitle():
        kol += 1
print("""У тексті з Великої літери починається:""",kol,"слів")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("======================")
print("""Виведіть позицію, на якій слово Tom зустрічається вдруге""")
index = adwentures_of_tom_sawer.find("Tom")
if index != -1:
    second_index = adwentures_of_tom_sawer.find("Tom", index + 1)
    if second_index != -1:
        print(f"Toma pнайдено на позиції {second_index}")
else:
    print("Tom втік")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("======================")
print("Розділіть змінну adwentures_of_tom_sawer по кінцю речення.")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("======================")
print("Виведіть четверте речення з adwentures_of_tom_sawer_sentences")
predlozenie4 = adwentures_of_tom_sawer_sentences[3]
print(predlozenie4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("======================")
print("""Перевірте чи починається якесь речення з "By the time""")
find_by = adwentures_of_tom_sawer.find("By the time")
if find_by != -1:
    print(f"Речення знайдено на позиції {find_by}.")
else:
    print("Речення не знайдено.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("======================")
print("""Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences""")
posled_predl = adwentures_of_tom_sawer_sentences[-1]
#print(posled_predl)
slova = posled_predl.split()
#print(slova)
kol_slov = len(slova)
#print(kol_slov)
print(f"Кількість слів останнього речення: {kol_slov}.")