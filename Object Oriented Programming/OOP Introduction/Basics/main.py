from Student import Student
from StudentGroup import StudentGroup

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

    print(myClass.getStudent(4).getName())

    print(myClass.getAllStudents())
    myClass.printTheStudentsListNicely(myClass.getAllStudents())


    
