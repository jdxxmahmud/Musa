from companyCreation import *

def rankCompanies(companyList):
    # This function will rank companies based on their annual profit
    pass


def startProject():
    myCompanyList = []

    myCompanyList.append(addDetailsForCompany1())
    myCompanyList.append(addDetailsForCompany2())
    myCompanyList.append(addDetailsForCompany3())
    
    if input("Do you want to get the detais of Company?   [y/n]\t\t").lower() == "y":
        for company in myCompanyList:
            print(company.getName())


    rankCompanies(myCompanyList[:])

if __name__ == "__main__":
    startProject()

