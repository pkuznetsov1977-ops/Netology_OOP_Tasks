class Student:
    def __init__(self,name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self,lecturer,course,grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self,course_name):
        self.finished_courses.append(course_name)
    def average_grade(self):
        grades_list = self.grades.values()
        return sum(grades_list)/len(grades_list)
    def __str__(self) -> str:
        return (f'Имя: {self.name} \n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}\n')
    def __gt__(self,other):
        if isinstance(other,Student):
            return self.average_grade() > other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'

    def __eq__(self,other):
        if isinstance(other,Student):
            return self.average_grade() == other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'
    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'
    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'
    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'
class  Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self,student,course,grade):
        if isinstance(student,Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def rate_hw(self):
        pass
    def average_grade(self):
        grades_list = self.grades.values()
        return sum(grades_list)/len(grades_list)
    def __str__(self) -> str:
        return f'Имя: {self.name} \n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_grade()}\n'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только лекторов между собой.'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только лекторов между собой.'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только лекторов между собой.'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только лекторов между собой.'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только студентов между собой.'

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        else:
            return 'Ошибка. Можно сравнивать только лекторов между собой.'

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)
    def __str__(self) -> str:
        return f'Имя: {self.name} \n Фамилия: {self.surname}\n'

