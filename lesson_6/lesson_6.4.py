print("""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті""")
print("-"*60)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for even_numbers in list1:
    if even_numbers % 2 == 0: # PyCharm по сути за меня написал задачу) Концептуально я понял что хочу, но правильную проверку он сам предугадал, мне осталось только нажать Tab. Докиньте пару балов ему за помощь)
        even_list.append(even_numbers)
sum_list = sum(even_list)
print(sum_list)
