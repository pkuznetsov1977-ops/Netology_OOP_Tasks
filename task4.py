from typing import List


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
                return f'Выставлена оценка: {grade} по курсу {course} лектору: {lecturer.name} {lecturer.surname} студентом {self.name} {self.surname}'
            else:
                lecturer.grades[course] = [grade]
                return f'Выставлена оценка: {grade} по курсу {course} лектору: {lecturer.name} {lecturer.surname} студентом {self.name} {self.surname}'
        else:
            return 'Ошибка'

    def add_courses(self,course_name):
        self.finished_courses.append(course_name)
    def average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            all_grades += grade_list
        return sum(all_grades)/len(all_grades)
    def __str__(self) -> str:
        return (
                f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {str(self.average_grade())}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n')
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
                return f'Выставлена оценка: {grade} по курсу {course} студенту: {student.name} {student.surname}  преподавателем {self.name} {self.surname}'
            else:
                student.grades[course] = [grade]
                return f'Выставлена оценка: {grade} по курсу {course} студенту: {student.name} {student.surname}  преподавателем {self.name} {self.surname}'
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def rate_hw(self):
        pass
    def average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            all_grades += grade_list
        return sum(all_grades) / len(all_grades)
    def __str__(self) -> str:
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'

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
        return super().rate_hw(student, course, grade)
    def __str__(self) -> str:
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'

def students_average_grade(students_list : list[Student], course: str) -> float:
    if  isinstance(students_list, list):
        grades_list = []
        for student in students_list:
            if isinstance(student, Student) and course in student.courses_in_progress:
                grades_list += student.grades.get(course,[])
        if len(grades_list) == 0:
            return 0
        else:
            return sum(grades_list) / len(grades_list)

def lecturers_average_grade(lecturers_list : list[Lecturer], course: str) -> float:
    if  isinstance(lecturers_list, list):
        grades_list = []
        for lecturer in lecturers_list:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                grades_list += lecturer.grades.get(course,[])
        if len(grades_list) == 0:
            return 0
        else:
            return sum(grades_list)/len(grades_list)

lecturer1 = Lecturer('Иван','Иванов')
lecturer2 = Lecturer('Александр','Александров')
reviewer1 = Reviewer('Петр','Петров')
reviewer2 = Reviewer('Сергей','Сергеев')
student1 = Student('Алехина','Ольга','Ж')
student2 = Student('Еременко','Иван','М')
student1.courses_in_progress += ['Python','Java']
lecturer1.courses_attached += ['Python','C++']
reviewer1.courses_attached += ['Python','C++']

student1.courses_in_progress += ['Python','Java']
lecturer1.courses_attached += ['Python','C++']
reviewer1.courses_attached += ['Python','C++']
student2.courses_in_progress += ['C++','Java']
lecturer2.courses_attached += ['Java','C++']
reviewer2.courses_attached += ['Java','C++']
print(student1.rate_lecturer(lecturer1,'Python',7))
print(student1.rate_lecturer(lecturer1,'Java',8))
print(student1.rate_lecturer(lecturer1,'C++',8))
print(student1.rate_lecturer(lecturer2,'Java',9))
print(student1.rate_lecturer(lecturer2,'Python',6))
print(student1.rate_lecturer(lecturer1,'C++',8))
print(student2.rate_lecturer(lecturer1,'Python',9))
print(student2.rate_lecturer(lecturer1,'Java',9))
print(student2.rate_lecturer(lecturer1,'C++',9))
print(student2.rate_lecturer(lecturer2,'Java',9))
print(student2.rate_lecturer(lecturer2,'C++',6))
print(student2.rate_lecturer(lecturer2,'Python',9))
print(reviewer1.rate_hw(student1,'Python',8))
print(reviewer1.rate_hw(student1,'Python',9))
print(reviewer2.rate_hw(student1,'Java',9))
print(reviewer2.rate_hw(student2,'C++',7))
print(reviewer1.rate_hw(student2,'C++',6))
print (student1)
print(student2)
print (lecturer1)
print (lecturer2)
print (reviewer1)
print (reviewer2)
print(student1 > student2)
print(student2 > student1)
print(student1 == student2)
print(student1 != student2)
print(student1 >= student2)
print(student1 <= student2)
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)
print(lecturer1 >= lecturer2)
print(lecturer1 <= lecturer2)
student_list = [student1,student2]
lecturer_list = [lecturer1,lecturer2]
print(students_average_grade(student_list,'C++'))
print(lecturers_average_grade(lecturer_list, 'Java'))
