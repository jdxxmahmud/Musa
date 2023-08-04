from datetime import date
from employee import Employee
from company import Company
from manager import Manager

def rankCompanies(companyList):
    # This function will rank companies based on their annual profit
    pass

def addDetailsForCompany1():
    company1 = Company(date(1999, 10, 10), "Supermax", "Dhaka", "Large")
    #add 10 employees
    company1.addEmployee(Manager(company1.getEmployeeId(), "Jamil", 100000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Nafis", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Radian", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Samiur", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Abdullah", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Ayan", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Musa", "Staff", 40000))

    print("Company 1 created")
    if input("Do you want to get the detais of Company 1?   [y/n]\t\t").lower() == "y":
        company1.printCompanyDetails()
    

    return company1

def startProject():
    myCompanyList = []

    company1 = addDetailsForCompany1()
    

    
    # company2 = addDetailsForCompany2()
    # company2.printCompanyDetails()



if __name__ == "__main__":
    startProject()

