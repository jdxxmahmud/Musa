class Student:
    def __init__(self, name, grade, age, marks):
        self.name = name 
        self.grade = grade 
        self.age = age 
        self.marks = marks

    def get_name(self):
        return self.name 
    def get_age(self):
        return self.age
    def get_marks(self):
        return self.marks
    def get_grade(self):
        return self.grade



s1 = Student('Musa', 9, 17, 98)

print(s1.get_name())
from student import Student

s2 = Student('Musa', 10, 'B', 98, '202010B')

print(s2.get_studentID())