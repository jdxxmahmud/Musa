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
        days = datetime.today() - self.joiningDate
        days = (days.days)

        years  = days // 365
        days = (days % 365)

        months = days // 30 
        days = days % 30
       
        # months = (days - (years*365)) / 30 
        # if months < 1:
        #     days = (days - (years*365))
        #     months = 0 
        # else:
        #     days = int((months - int(months)) * 30)
        #     months = int(months)  

        return years, months, days

    def printFullDetails(self):
        print(f'Employee ID: {self.getId()}\nName: {self.getName()}\nPosition: {self.getPosition()}\nSalary: {self.getSalary()}\nJoining Date: {self.getJoiningDate()}\n')
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
    
