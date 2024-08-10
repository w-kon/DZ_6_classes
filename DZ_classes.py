class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) 
            and course in lecturer.courses_attached 
            and (course in self.courses_in_progress or course in self.finished_courses)
            and grade >=1 and grade <=10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_rating(self):
        if len(self.grades) != 0:
            resalt = []
            for value in self.grades.values():
                resalt.extend(value)
            return (sum(resalt)/len(resalt))
        else: return "Оценок нет"
        
    def __str__(self) -> str:
        return(f"Имя: {self.name} \nФамилия: {self.surname}\n\Средняя оценка за домашние задания: {Student.average_rating(self)}\n\Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n\Завершенные курсы: {', '.join(self.finished_courses)}\n")

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        if len(self.grades) != 0:
            resalt = []
            for value in self.grades.values():
                resalt.extend(value)
            return (sum(resalt)/len(resalt))
        else: return "Оценок нет"

    def __str__(self) -> str:
        return(f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекцию: {Lecturer.average_rating(self)}\n")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) 
            and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return(f"Имя: {self.name} \nФамилия: {self.surname}\n")

 
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'QA']
student_1.finished_courses += ['Web']

student_2 = Student('Mark', 'Eman', 'your_gender')
student_2.courses_in_progress += ['Web', 'Java'] 
student_2.finished_courses += ['Python']

student_3 = Student('Mark', 'Eman', 'your_gender')
student_3.courses_in_progress += ['Web', 'Java', 'Python'] 
student_3.finished_courses += []
 
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java', 'QA', 'Web']

lecturer_1 = Lecturer('Scott', 'Buddy')
lecturer_1.courses_attached += ['Python', 'Java', 'Web']
 
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'QA', 10)
reviewer_1.rate_hw(student_2, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Web', 9)
reviewer_1.rate_hw(student_2, 'Pyton', 8)

student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Web', 1)
student_2.rate_hw(lecturer_1, 'Web', 10)
student_2.rate_hw(lecturer_1, 'Java', 9)
student_2.rate_hw(lecturer_1, 'Python', 5)
student_3.rate_hw(lecturer_1, 'Python', 8)
student_3.rate_hw(lecturer_1, 'Java', 10)


print(student_1)
print(reviewer_1)
print(lecturer_1)
#print(lecturer_1.grades)
# print(student_1.grades)
# print(student_2.grades)
# print(Student.average_rating(student_3))