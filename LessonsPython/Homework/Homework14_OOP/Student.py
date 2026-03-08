class Student:
    name: str
    surname: str
    age: int
    grades: list[float]

    def __init__(self, name, surname, age, grades=None) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        if grades == None:
            self.grades = []
        else:
            self.grades = grades

    # добавление оценки студенту
    def add_grade(self, grade):
        self.grades.append(grade)
        
    # возвращает среднюю оценку студента
    def get_average_grade(self):
        sum = 0
        for grade in self.grades:
            sum += grade

        average_grade = sum / len(self.grades)
        return average_grade

    # возвращает информацию о студенте
    def get_info(self):
        average_grade = self.get_average_grade()
        print(f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}, Средняя оценка: {average_grade:.2f}")
        

# pupil1 = Student("аа", "бб", 15)
# pupil1.add_grade(5)
# pupil1.add_grade(4)
# pupil1.add_grade(4)
# pupil1.get_info()