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

def addDetailsForCompany2():
    company2 = Company(date(1887, 9, 10), "Anaconda", "Amazon", "Large")
    #add 10 employees
    company2.addEmployee(Manager(company2.getEmployeeId(), "Mahboub", 100000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Mahtab", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Zayed", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Sumaiya", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Zunaira", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Fahad", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Tasnuba", "Staff", 40000))

    print("Company 2 created")
    if input("Do you want to get the detais of Company 2?   [y/n]\t\t").lower() == "y":
        company2.printCompanyDetails()
    
    return company2


def addDetailsForCompany3():
    company3 = Company(date(2002, 3, 5), "KC", "Dhaka", "Large")
    #add 10 employees
    company3.addEmployee(Manager(company3.getEmployeeId(), "Abul", 100000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mahajabeen", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mahir", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Sami", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Junayed", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Lamisa", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mowrin", "Staff", 40000))

    print("Company 3 created")
    if input("Do you want to get the detais of Company 3?   [y/n]\t\t").lower() == "y":
        company3.printCompanyDetails()
    
    return company3



def startProject():
    myCompanyList = []

    company1 = addDetailsForCompany1()
    company2 = addDetailsForCompany2()
    company3 = addDetailsForCompany3()
    

    
    # company2 = addDetailsForCompany2()
    # company2.printCompanyDetails()



if __name__ == "__main__":
    startProject()

