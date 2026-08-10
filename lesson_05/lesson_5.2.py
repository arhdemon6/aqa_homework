# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
#from main import print_hi

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list
print(f"===========================================================")
print(f"# 1 - Add your new record o the beginning of the given list:")
new_people = ('Dmytro', 'Ostapenko', 36, 'QA', 'Kharkiv') #решил добавить себя любимого
print(f"Новый человек в команде:\n"
      f"Имя - {new_people[0]} \n"
      f"Фамилия - {new_people[1]} \n"
      f"Лет - {new_people[2]}\n"
      f"Должность - {new_people[3]}\n"
      f"Город - {new_people[4]}")
print(f"Новый список команды:")
people_records.insert(0,new_people)
i = 0
for person in people_records:
    print(i,person)
    i += 1

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print(f"===========================================================")
print(f"2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result.")
print(f"Список команды:")
i = 0
for person in people_records:
    print(i,person)
    i += 1

print(f"Список команды после:")
people_records[1], people_records[5] = people_records[5], people_records[1]

i = 0
for person in people_records:
    print(i,person)
    i += 1

print(f"===========================================================")
print(f"# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result")

print_hi = people_records[6], people_records[10] ,people_records[13]
print("Работкики на позициях 6, 10 и 13 по индексу:")
print(print_hi)

all_match = True
for person in print_hi:
    if person[2] >= 30:
        continue
    else:
        all_match = False
        break

if all_match:
    print("Все работники из списка миллениалы!")
else:
    print("В команде присутствуют зумеры (-_-)")