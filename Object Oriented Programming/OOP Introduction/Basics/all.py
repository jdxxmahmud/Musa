class Student:
    def __init__(self, id: int, name: str, age: int):
        #Private 
        self.__id = id
        self.__name = name 
        self.__age = age

    #Getter Methods - Private 
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

    #Setter Methods - Private 
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name
    
    def setAge(self, age):
        self.__age = age

class StudentGroup:
    def __init__(self):
        self.__student_list = []

    def addStudent(self, student: Student):
        self.__student_list.append(student)

    def getStudent(self, id):
        for student in self.__student_list:
            if student.getId() == id:
                return student

    def getAllStudents(self):
        lst = []
        for student in self.__student_list:
            lst.append([student.getId(), student.getName(), student.getAge()])
        return lst 

    def printTheStudentListNicely(self, students):
        for student in students:
            print(f"Id: {student[0]}, Name: {student[1]}, Age: {student[2]}")

if __name__ == "__main__":
    myClass = StudentGroup()
    myClass.addStudent(Student(1, "Musa", 15))
    myClass.addStudent(Student(2, "Nafis", 16))
    myClass.addStudent(Student(3, "Afifa", 14))
    myClass.addStudent(Student(4, "Radian", 17))
    myClass.addStudent(Student(5, "Samiul", 19))
    myClass.addStudent(Student(6, "Fahim", 16))
    myClass.addStudent(Student(7, "Tasnuva", 12))
    myClass.addStudent(Student(8, "Shikhi", 16))
    myClass.addStudent(Student(9, "Mushfiq", 15))

    print(myClass.getAllStudents())

    myClass.printTheStudentListNicely(myClass.getAllStudents())


    