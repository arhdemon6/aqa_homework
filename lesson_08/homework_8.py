
print("""Задание:"Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу, представляючи студента. 
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. 
Виведіть інформацію про студента та змініть його середній бал.""")

class Student:

    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_average_grade):
        """меняем средний балл"""
        self.average_grade = new_average_grade

    def show_info(self):
        """Выводим информацию про студента"""
        print(f'Имя: {self.first_name}')
        print(f'Фамилия: {self.last_name}')
        print(f'Возраст: {self.age}')
        print(f'Средний балл: {self.average_grade}')

student1 = Student("Василий", "Пупкин", 30, 7.5)

print("Студент:")
student1.show_info()

# тут меняем средний балл
student1.change_average_grade(9.0)

print("\nСтудент после изменения среднего балла:")
student1.show_info()