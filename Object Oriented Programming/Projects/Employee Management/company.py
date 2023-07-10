from datetime import date
from employee import Employee 


class Company:

    employeeId = 0
    revenue = None
    cost = None

    def __init__(self, foundingDate, name, location, industry):
        self.foundingDate = foundingDate
        self.name = name
        self.location = location
        self.industry = industry

        self.employeeList = []

    def addEmployee(self, employee: Employee):
        self.employeeList.append(employee)
        self.employeeId += 1


    def showEmployeeList(self, id):
        for i in self.employeeList:
            if self.employeeList[i].getId() == id:
                return f'ID:{self.employeeList[i].getId()}\nName:{self.employeeList[i].getName()}\nPosition:{self.employeeList[i].getPosition()}'

    def allocatedAmountOfProfitSharingForEmployees():
        # this will return the amount of profit that will be given to each employee
        # only applicable for the employee who has working year more than 1
        pass
        
    def findEmployeeById():
        # This function will return all the details of an employee based on the ID
        pass

    def findEmployeeByName():
        # This function will return all the details of an employee based on the name
        # here the actual name will be title case. 
        # but searched text can be small letter
        pass

    def addProfitSharingWithTheSalary():
        # This will print the employee name and their salary (after addition of profit sharing with salary)
        pass

    #Getter methods
    def getFoundingDate(self):
        return self.foundingDate
        
    def getName(self):
        return self.name
        
    def getLocation(self):
        return self.location
        
    def getIndustry(self):
        return self.industry
        
    def getTotalEmployees(self):
        return len(self.employeeList)
        
    def getRevenue(self):
        return self.revenue

    def getCost(self):
        return self.cost
    
    def getEmployeeId(self):
        return self.getEmployeeId
        

    #Setter methods    
    def setFoundingDate(self, foundingDate):
        self.foundingDate = foundingDate
        
    def setName(self, name):
        self.name = name
        
    def setLocation(self, location):
        self.location = location
        
    def setIndustry(self, industry):
        self.industry = industry
        
    def setRevenue(self, revenue):
        self.revenue = revenue

    def setCost(self, cost):
        self.cost = cost

    def setEmployeeId(self, employeeId):
        self.employeeId = employeeId