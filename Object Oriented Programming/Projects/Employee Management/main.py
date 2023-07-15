from datetime import date
from employee import Employee
from company import Company

def rankCompanies(companyList):
    # This function will rank companies based on their annual profit
    pass



def addDetailsForCompany1():
    company1 = Company(date(1999, 10, 10), "Supermax", "Dhaka", "Large")
    #add 10 employees
    company1.addEmployee(Employee("Jamil", "Staff", 40000))




company1 = addDetailsForCompany1()

print(company1)


