'''
attributes, methods to the employee class{name, id, salary, position, joining date}
methods:
i.Numberofyears employee have been working based on joining date
company -
'''
from datetime import date

class employee:
    def __init__(self, id, name, position, joining_date, salary):
        self.name = name 
        self.id = id 
        self.position = position
        self.joining_date = joining_date
        self.salary = salary

    #Getter Methods - 
    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position

    def getJoining_Date(self):
        return self.joining_date
    
    def getSalary(self):
        return self.salary

    #Setter Methods 
    def setId(self, id):
        self.id = id 

    def setName(self, name):
        self.name = name 

    def setPosition(self, position):
        self.position = position
    
    def setJoining_date(self, joining_date):
        self.joining_date = joining_date

    def setSalary(self, salary):
        self.salary = salary 
    
    #Functional Methods 
    def Numberofyears(self):
        return (date.today() - self.joining_date)

    

