# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True: #тут нужен бесконечный цикл
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25: #cравнивали со строкой "25"
            # Enter the action to take if the result is greater than 25
            break # c pass мы бы просто продолжали бесконечный цикл, а не выбрасывались с него.
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1 # переменной multi нет и не было) ну и таб лишний был

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("-"*60)
def sum_number(number1, number2):
    result  = number1 + number2
    return result
print(sum_number(3, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("-"*60)
def average (numbers):
    result = sum(numbers) / len(numbers)
    return result

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(text):
    result = ''
    for char in text:
        result = char + result
    return result

print(reverse_string('Hello AQA'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("-"*60)
def longest_word(words):
    longest = words[0]
    for word in words[1:]: #использовать подсказки PyCharm не читерство)
        if len(word) > len(longest_word):
            longest = word
    return longest

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    for i in range(len1 - len2 + 1):
        if str1[i:i + len2] == str2:
            return i

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 Домашка 3 задание 10
def journey(distance, gas_consumption, tank):

    total_gasoline = (distance/100) * gas_consumption
    number_of_refills= total_gasoline / tank
    return number_of_refills, total_gasoline

# task 8 Домашка 6.3
def only_string(items):

    lst_str = []
    for item in items:
        if isinstance(item, str):
            lst_str.append(item)
    return lst_str

# task 9 Домашка 6.4
def sum_of_even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    total = sum(even_list)
    return total

# task 10 Домашка 6.2
def word_with_h():
    attempts = 0
    while True:
        word = input('Введите слово с буквой "h": ')
        attempts += 1
        if 'h' in word.lower():
            print(f'''Невероятно! Просто безумие! Слово "{word}" содержит букву "H/h"''')
            print(f'Вы сдались всего на какой-то: {attempts} раз')
            break
word_with_h()