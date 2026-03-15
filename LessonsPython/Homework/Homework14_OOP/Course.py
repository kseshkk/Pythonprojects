from Student import Student

class Course:
    students: list[Student]

    def __init__(self) -> None:
        self.students = []

    # добавление студента в курс
    def add_student(self, student: Student) -> None:
        self.students.append(student)

    # возвращает студента с наибольшей средней оценкой
    def get_best_student(self):
        self.students.sort(key=lambda student: student.get_average_grade(),reverse=True)
        return self.students[0]
    
    # вывод всех студентов курса
    def print_all_students(self):
        for item in self.students:
            item.get_info()


    