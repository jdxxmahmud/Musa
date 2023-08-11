from companyCreation import *
from company import Company

def rankCompanies(companyList):
    for companies in range(len(companyList)):
        for company in range(len(companyList) - companies - 1):
            if companyList[company].getRevenue() < companyList[company + 1].getRevenue():
                temporary = companyList[company]
                companyList[company] = companyList[company + 1]
                companyList[company + 1] = temporary
    
    return companyList

def startProject():
    myCompanyList = []

    myCompanyList.append(addDetailsForCompany1())
    myCompanyList.append(addDetailsForCompany2())
    myCompanyList.append(addDetailsForCompany3())
    myCompanyList.append(addDetailsForCompany4())
    myCompanyList.append(addDetailsForCompany5())
    
    if input("Do you want to get the detais of Company?   [y/n]\t\t").lower() == "y":
        for company in myCompanyList:
            print(company.getName())


    rankedCompanyList = rankCompanies(myCompanyList[:])

    for company in rankedCompanyList:
        print(company.getName())

if __name__ == "__main__":
    startProject()

