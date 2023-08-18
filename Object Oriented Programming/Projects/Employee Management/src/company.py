from datetime import date
from time import sleep
from employee import Employee 


class Company:
    
    def __init__(self, foundingDate, name, location, industry, revenue = 0, cost = 0):
        self.employeeId = 1
        self.foundingDate = foundingDate
        self.name = name
        self.location = location
        self.industry = industry
        self.revenue = revenue
        self.cost = cost
        self.employeeList = []
        self.employeeId = 1

    def addEmployee(self, employee: Employee):
        self.employeeList.append(employee)
        self.employeeId += 1
        
    
        # this will return the amount of profit that will be given to each employee who are working for more than 1 year
    def allocatedAmountOfProfitSharingForEmployees(self):
        employeeCount = 0 #employee working for more than a year
        for i in self.employeeList:
            if self.employeeList[i].numberOfYears()[0] >= 1:
                employeeCount += 1
        return f'{(Company.revenue - Company.cost) / employeeCount} to each {employeeCount} employee' 

        # This function will return all the details of an employee based on the ID
    def findEmployeeById(self, id):
        for i in self.employeeList:
            if self.employeeList[i].getId() == id:
                return f'ID:{self.employeeList[i].getId()}\nName:{self.employeeList[i].getName()}\nPosition:{self.employeeList[i].getPosition()}'


        # This function will return all the details of an employee based on the name
    def findEmployeeByName(self, name):
        for i in self.employeeList:
            if self.employeeList[i].getName().lower() == name.lower():
               return f'ID:{self.employeeList[i].getId()}\nName:{self.employeeList[i].getName()}\nPosition:{self.employeeList[i].getPosition()}' 


    # This will print the employee name and their salary (after addition of profit sharing with salary)
    def addProfitSharingWithTheSalary(self, employee: Employee):
        if employee.joiningDate() - date.today > date(1, 0, 0):
            print(f'Employee:{employee.getName()}\nSalary: {employee.getSalary() + self.allocatedAmountOfProfitSharingForEmployees()}')
        else:
            print(f"Employee:{employee.getName()}\nSalary: {employee.getSalary()}")
        

    def printCompanyDetails(self):
        print(f'Company Name: {self.getName()}')
        print(f'Location: {self.getLocation()}')
        print(f'Fouding Date: {self.getFoundingDate()}')

        print("\nPrinting employee details \n\n")
        for employee in self.employeeList:
            sleep(.2)
            employee.printFullDetails()

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
        return self.employeeId
        

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

        