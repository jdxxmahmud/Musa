from datetime import date
from employee import Employee
from company import Company
from manager import Manager
from generalManager import GeneralManager

def addDetailsForCompany1():
    company1 = Company(date(1999, 10, 10), "Supermax", "Dhaka", "Large", 100000)
    #add 10 employees
    company1.addEmployee(Manager(company1.getEmployeeId(), "Jamil", 100000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Nafis", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Radian", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Samiur", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Abdullah", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Ayan", "Staff", 40000))
    company1.addEmployee(Employee(company1.getEmployeeId(), "Musa", "Staff", 40000))

    print("Company 1 created")
    # if input("Do you want to get the detais of Company 1?   [y/n]\t\t").lower() == "y":
    #     company1.printCompanyDetails()
    
    return company1

def addDetailsForCompany2():
    company2 = Company(date(1887, 9, 10), "Anaconda", "Amazon", "Large", 50000)
    #add 10 employees
    company2.addEmployee(Manager(company2.getEmployeeId(), "Mahboub", 100000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Mahtab", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Zayed", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Sumaiya", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Zunaira", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Fahad", "Staff", 40000))
    company2.addEmployee(Employee(company2.getEmployeeId(), "Tasnuba", "Staff", 40000))

    print("Company 2 created")
    # if input("Do you want to get the detais of Company 2?   [y/n]\t\t").lower() == "y":
    #     company2.printCompanyDetails()
    
    return company2


def addDetailsForCompany3():
    company3 = Company(date(2002, 3, 5), "KC", "Dhaka", "Large", 150000)
    #add 10 employees
    company3.addEmployee(Manager(company3.getEmployeeId(), "Abul", 100000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mahajabeen", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mahir", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Sami", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Junayed", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Lamisa", "Staff", 40000))
    company3.addEmployee(Employee(company3.getEmployeeId(), "Mowrin", "Staff", 40000))

    print("Company 3 created")
    # if input("Do you want to get the detais of Company 3?   [y/n]\t\t").lower() == "y":
    #     company3.printCompanyDetails()
    
    return company3

def addDetailsForCompany4():
    company4 = Company(date(1969, 2, 8), "Mattle", "Ohio", "Milk", 350000)
    #employees
    company4.addEmployee(GeneralManager(company4.getEmployeeId(), "Kuddus", 100000))
    company4.addEmployee(Manager(company4.getEmployeeId(), "Enamul", 70000))

    print('Company 4 created')

    return company4


def addDetailsForCompany5():
    company5 = Company(date(1989, 4, 8), "Lolly", "wakanda", "cotton", 750000)
    #employees
    company5.addEmployee(GeneralManager(company5.getEmployeeId(), "selim", 100000))
    company5.addEmployee(Manager(company5.getEmployeeId(), "rawshan", 70000))

    print('Company 5 created')

    return company5