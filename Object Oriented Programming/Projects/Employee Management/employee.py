'''
attributes, methods to the employee class{name, id, salary, position, joining date}
methods:
i.Numberofyears employee have been working based on joining date
company -
'''
from datetime import date

class Employee:

    def __init__(self, id, name, position, salary):
        self.id = id 
        self.name = name 
        self.position = position
        self.joiningDate = None ## Automatically add the joining date using datetime 
        self.salary = salary

    def yearlySalaryIncrement(self):
        # this function will increase and set the salary by 10% when called.
        pass

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

    

