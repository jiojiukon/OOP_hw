def avg_grades(grade):
    mean = 0
    grades_count = 0
    if len(grade.values()) > 0:
        for course in grade.values():
            mean += sum(course)
            grades_count += len(course)
        return mean / grades_count
    else:
        return f'Нет оценок'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['aaa', 'addd']
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Студентов сравниваем только со студентами!')
            return
        return avg_grades(self.grades) > avg_grades(other.grades)

    def __str__(self):
            return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {avg_grades(self.grades)}
Курсы в процессе обучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
"""    

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

 
class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grades(self.grades)}'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лекторов сравниваем только с лекторами!')
            return
        return avg_grades(self.grades) > avg_grades(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Pavel', 'Durov', 'male')
best_student.courses_in_progress += ['Python','C++']


bad_student = Student('Denis','Dorohov','male')


cool_rewiewer = Reviewer('Some', 'Buddy')
cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.rate_hw(best_student, 'Python', 10)
cool_rewiewer.rate_hw(best_student, 'C++', 10)
cool_rewiewer.rate_hw(best_student, 'Python', 10)

cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.rate_hw(bad_student, 'Python', 3)
cool_rewiewer.rate_hw(bad_student, 'Python', 5)

best_lecturer = Lecturer('Miron', 'Fedorov')
best_lecturer.courses_attached += ['C++', 'Python']

bad_lecturer = Lecturer('Ivan', 'Ohlibystin')
bad_lecturer.courses_attached += ['C++', 'Python']

bad_student.rate_lecture(best_lecturer, 'Python', 4)
best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'C++', 9)

bad_student.rate_lecture(best_lecturer, 'Python', 4)
best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'C++', 9)
bad_student.rate_lecture(bad_lecturer, 'Python', 4)
best_student.rate_lecture(bad_lecturer, 'Python', 2)
best_student.rate_lecture(bad_lecturer, 'C++', 3)

print(f'Лучший студент - {best_student.name} с оценками: {best_student.grades}')
print(f'Уроки лектора {best_lecturer.name} оценили {best_lecturer.grades}')

print(best_student)
print(bad_student)
print(best_lecturer)
print(bad_lecturer)

print(cool_rewiewer)

print(best_lecturer > bad_lecturer)
print(best_lecturer < bad_lecturer)