class Student:
    def __init__(self, name, sector):
        self.name = name 
        self.sector = sector


    def get_student():
        student = Student()
        student.name = input('Name:')
        student.sector = input('Sector:')

get_student()

print(f'{student.name} from {student.sector}')
