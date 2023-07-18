'''
attributes, methods to the employee class{name, id, salary, position, joining date}
methods:
i.Numberofyears employee have been working based on joining date
company -
'''
from datetime import datetime



class Employee():

    def __init__(self, id, name, position, salary, joiningDate = datetime.today()):
        self.id = id
        self.name = name 
        self.position = position
        self.salary = salary
        self.joiningDate = joiningDate


    # this function will increase and set the salary by 10% when called.
    def yearlySalaryIncrement(self):
        self.salary = round(self.salary * 1.1, 2)

    # will return total working days in years, months and dates.
    def numberOfYears(self):
        return (datetime.today() - self.joiningDate)

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
    
