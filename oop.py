main_dic = {}
avg_dic = {}

def avg_(grade):
    for k, v in grade.items():
        if k in main_dic.keys():
            main_dic[k] += [sum(v)//len(v)]
        else:
             main_dic[k] = [sum(v)//len(v)]
    for y,i in main_dic.items():
        i = sum(i)/len(i)
        avg_dic[y] = i
    return 


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
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades_on_course = {}
        

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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grades(self.grades)}\n'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лекторов сравниваем только с лекторами!')
            return
        return avg_grades(self.grades) > avg_grades(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


best_student = Student('Pavel', 'Durov', 'male')
best_student.courses_in_progress += ['Python','C++']

worst_student = Student('Denis','Dorohov','male')
worst_student.courses_in_progress += ['Python']

cool_rewiewer = Reviewer('Some', 'Buddy')
cool_rewiewer.rate_hw(best_student,'Python', 9)
cool_rewiewer.rate_hw(best_student,'C++', 10)
cool_rewiewer.rate_hw(worst_student,'Python', 3)

cool_lecturer = Lecturer('Miron','Federov')
cool_lecturer.courses_attached += ['Python','C++']
bad_lecturer = Lecturer('Ivan', 'Ohlobystin')
bad_lecturer.courses_attached += ['Python']

best_student.rate_lecture(cool_lecturer,'Python', 9)
best_student.rate_lecture(cool_lecturer,'C++', 8)
best_student.rate_lecture(bad_lecturer,'Python', 3)
worst_student.rate_lecture(cool_lecturer,'Python', 7)
worst_student.rate_lecture(bad_lecturer,'Python', 5)

print(best_student)
print(worst_student)

print(cool_rewiewer)
print(cool_lecturer)
print(bad_lecturer)

print(cool_lecturer.grades)
print(bad_lecturer.grades)
print(best_student.grades)
print(worst_student.grades)

avg_(cool_lecturer.grades)
avg_(bad_lecturer.grades)
avg_(best_student.grades)
avg_(worst_student.grades)
print('__________________')

print(avg_dic)

print(cool_lecturer.grades)

print(cool_lecturer > bad_lecturer)
print(cool_lecturer < bad_lecturer)