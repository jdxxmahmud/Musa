'''
company -
list of employee 
and the class company will have it's own attributes{revenue, company type}
methods 
multiple classes, multiple files 
method :
i.profit() 
i.add profit with the salary conda clean --helpconda clean --helpconda clean --help
'''
from datetime import date
from employee import Employee 


class Company:
    def __init__(self, foundingDate, name, location, industry, totalEmployees, revenue, profit):
        self.foundingDate = foundingDate
        self.name = name
        self.location = location
        self.industry = industry
        self.totalEmployees = totalEmployees
        self.revenue = revenue
        self.profit = profit

        self.employeeList = []

    def addEmployee(self, employee: employee):
        self.employeeList.append(employee)

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
        return self.totalEmployees
        
    def getRevenue(self):
        return self.revenue

    def getProfit(self):
        return self.profit
        
    def getEmployee(self, id):
        for i in self.employeeList:
            if self.employeeList[i].getId() == id:
                return f'ID:{self.employeeList[i].getId()}\nName:{self.employeeList[i].getName()}\nPosition:{self.employeeList[i].getPosition()}' 

    #Setter methods    
    def setFoundingDate(self, foundingDate):
        self.foundingDate = foundingDate
        
    def setName(self, name):
        self.name = name
        
    def setLocation(self, location):
        self.location = location
        
    def setIndustry(self, industry):
        self.industry = industry

    def setTotalEmployees(self, totalEmployees):
        self.totalEmployees = totalEmployees
        
    def setRevenue(self, revenue):
        self.revenue = revenue

    def setProfit(self, profit):
        self.profit = profit