print("""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими""")
print("-"*60)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst_str = []
for item in lst1:
        if isinstance(item, str): #нашел в файле built-in-functions_3.py на предыдущем занятии) Долго пытался понять как отсеять
            lst_str.append(item)

print(lst_str)