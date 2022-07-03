class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_lect(self, lecturer, lecture, score):
        if isinstance(lecturer, Lecturer) and lecture in self.courses_attached and lecture in self.courses_in_progress:
            if lecture in lecturer.scores:
                lecturer.scores[lecture] += [score]
            else:
                lecturer.scores[lecture] = [score]
        else:
            return 'Ошибка'

    def av_grade(self):
        grades_list = []
        for i, n in self.grades.items():
            for grade in n:
                grades_list.append(grade)
        av_grade = round(sum(grades_list) / len(grades_list), 2)
        return av_grade

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Student:\n{self.name}\n{self.surname}\nСредняя оценка за домашние задания: {self.av_grade()}\nКурсы в процессе обучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.av_grade() < other.av_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.scores = {}


class Lecturer(Mentor):

    def av_score(self):
        scores_list = []
        for key, value in self.scores.items():
            for score in value:
                scores_list.append(score)
        av_score = round(sum(scores_list) / len(scores_list), 2)
        return av_score

    def __str__(self):
        return f"Lecturer:\n{self.name}\n{self.surname}\nСредняя оценка за лекции: {self.av_score()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.av_score() < other.av_score()


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
        return f"Reviewer:\n{self.name}\n{self.surname}"


lecturer_1 = Lecturer('Somelecturer', 'Buddylecturer')
lecturer_1.courses_attached += ['Python']

student_1 = Student('Ruoy', 'Eman', 'gender_1')
student_1.courses_in_progress += ['Python', 'Github']
student_1.courses_attached += ['Python', 'Github']
student_1.finished_courses += ['Введение в программирование']

student_1.rate_lect(lecturer_1, 'Python', 4)
student_1.rate_lect(lecturer_1, 'Python', 4)
student_1.rate_lect(lecturer_1, 'Python', 5)

reviewer_1 = Reviewer('SomeReviewer', 'BodyReviewer')
reviewer_1.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 4)

lecturer_2 = Lecturer('Morfius', 'Black')
lecturer_2.courses_attached += ['Python']

student_2 = Student('Neo', 'Anderson', 'gender_2')
student_2.courses_in_progress += ['Python', 'Github']
student_2.courses_attached += ['Python', 'Github']
student_2.finished_courses += ['Введение в программирование']

student_2.rate_lect(lecturer_2, 'Python', 5)
student_2.rate_lect(lecturer_2, 'Python', 5)
student_2.rate_lect(lecturer_2, 'Python', 5)

reviewer_2 = Reviewer('Trinity', 'love')
reviewer_2.courses_attached += ['Python']

reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)


print(f'Оценки студента 1 по Python:', student_1.grades)
print(f'Оценки лектора 1 по Python:', lecturer_1.scores)
print()
print(f'Оценки студента 2 по Python:', student_2.grades)
print(f'Оценки лектора 2 по Python:', lecturer_2.scores)
print()

print(reviewer_1)
print()
print(lecturer_1)
print()
print(student_1)
print()
print(reviewer_2)
print()
print(lecturer_2)
print()
print(student_2)
print()
