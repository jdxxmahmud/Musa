from Student import Student

class StudentGroup:
    def __init__(self):
        self.__student_list = []

    def addStudent(self, student: Student):
        self.__student_list.append(student)

    def getStudent(self, id):
        for student in self.__student_list:
            if student.getId() == id:
                return student

        # return None
    
    # This function will return a list of all the students
    def getAllStudents(self):
        lst = []
        for student in self.__student_list:
            lst.append([student.getId(), student.getName(), student.getAge()])
        return lst 


    # This function will take a list of students, and print them in the following format
    # Id: 1, Name: Musa, Age: 15
    # ...
    # ...
    def printTheStudentsListNicely(self, students):
        for student in students:
            print(f"Id: {student[0]}, Name: {student[1]}, Age: {student[2]}")