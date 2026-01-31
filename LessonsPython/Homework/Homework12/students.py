# Функция повышения класса
# Принимает объект Student и увеличивает номер класса на 1.

# Функция проверки возраста
# Принимает объект Student и возвращает True, если ученик совершеннолетний, иначе False.

# Функция сравнения двух учеников
# Принимает два объекта Student и определяет, кто из них старше, либо сообщает, что они ровесники.

# Функция проверки обучения в одном классе
# Принимает два объекта Student и возвращает True, если они учатся в одном классе.

# Функция изменения возраста
# Принимает объект Student и число лет, на которое нужно увеличить возраст ученика.


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int

def info(student: Student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def upgrade_grade(student: Student):
    if student.grade < 11:
        student.grade += 1
    return student.grade

def check_age(student: Student):
    if student.age >= 18:
        return True
    else:
        return False

def compare_students(student1: Student, student2: Student):
    if student1.age > student2.age:
        return f"{student1.name} старше чем {student2.name}"
    elif student1.age < student2.age:
        return f"{student2.name} старше чем {student1.name}"
    else:
        return f"{student1.name} и {student2.name} ровесники"
    
def check_same_class(student1: Student, student2: Student):
    if student1.grade == student2.grade:
        return True
    else:
        return False

def change_age(student: Student, raise_age):
    student.age += raise_age
    return student.age


student1 = Student("Иван", 14, 3)
student2 = Student("Мария", 13, 7)

info(student1)
info(student2)

# print(change_age(student1, 3))