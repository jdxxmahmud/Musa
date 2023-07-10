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
from employee import employee 


class company:
    def __init__(self, founding_date, name, location, industry, totalemployees, revenue, profit):
        self.founding_date = founding_date
        self.name = name
        self.location = location
        self.industry = industry
        self.totalemployees = totalemployees
        self.revenue = revenue
        self.profit = profit

        self.employee_list = []
    def addEmployee(self, employee: employee):
        self.employee_list.append(employee)


        #Getter methods
        def getFounding_date(self):
            return self.founding_date
        
        def getName(self):
            return self.name
        
        def getLocation(self):
            return self.location
        
        def getIndustry(self):
            return self.industry
        
        def getTotalEmployees(self):
            return self.totalemployees
        
        def getRevenue(self):
            return self.revenue

        def getProfit(self):
            return self.profit
        
        def getEmployee(self, id):
            for i in self.employee_list:
                if self.employee_list[i].getId() == id:
                    return f'ID:{self.employee_list[i].getId()}\nName:{self.employee_list[i].getName()}\nPosition:{self.employee_list[i].getPosition()}' 

        #Setter methods    
        def setFounding_date(self, founding_date):
            self.founding_date = founding_date
        
        def setName(self, name):
            self.name = name
        
        def setLocation(self, location):
            self.location = location
        
        def setIndustry(self, industry):
            self.industry = industry

        def setTotalEmployees(self, totalemployees):
            self.totalEmployees = totalEmployees
        
        def setRevenue(self, revenue):
            self.revenue = revenue

        def setprofit(self, profit):
            self.profit = profit