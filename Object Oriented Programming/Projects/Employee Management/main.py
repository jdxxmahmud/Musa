from datetime import date
from employee import Employee
from company import Company

def rankCompanies(companyList):
    # This function will rank companies based on their annual profit
    pass



def startProject():
    myCompanyList = []

    company1 = addDetailsForCompany1()
    company2 = addDetailsForCompany2()



if __name__ == "__main__":
    startProject()

def addDetailsForCompany1():
    company1 = Company(date(1999, 10, 10), "Supermax", "Dhaka", "Large")
    #add 10 employees
    company1.addEmployee(Employee(company1.getEmployeeId(), "Jamil", "Staff", 40000))


def addDetailsForCompany2():
    pass