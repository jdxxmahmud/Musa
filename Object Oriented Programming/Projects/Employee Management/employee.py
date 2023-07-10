'''
attributes, methods to the employee class{name, id, salary, position, joining date}
methods:
i.Numberofyears employee have been working based on joining date
company -
'''
from datetime import date

class Employee:
    def __init__(self, id, name, position, joiningDate, salary):
        self.name = name 
        self.id = id 
        self.position = position
        self.joiningDate = joiningDate
        self.salary = salary

    #Getter Methods - 
    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position

    def getJoiningDate(self):
        return self.joiningDate
    
    def getSalary(self):
        return self.salary

    #Setter Methods 
    def setId(self, id):
        self.id = id 

    def setName(self, name):
        self.name = name 

    def setPosition(self, position):
        self.position = position
    
    def setJoiningDate(self, joiningDate):
        self.joiningDate = joiningDate

    def setSalary(self, salary):
        self.salary = salary 
     
    def numberOfYears(self):
        return (date.today() - self.joiningDate)

    

