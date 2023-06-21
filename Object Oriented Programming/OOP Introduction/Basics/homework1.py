class Student:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    def getStudentInformation(self):
        return f'My student is: ID: {self.__id} and Name: {self.__name}'

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age


if __name__ == "__main__":

    myStudent = Student(1, 'Musa', 15)

    print(myStudent.getStudentInformation())
    myStudent.setAge(20)
    print(myStudent.getAge())
    
