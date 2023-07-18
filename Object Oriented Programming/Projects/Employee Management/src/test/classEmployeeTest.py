import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from employee import Employee
from company import Company
from datetime import datetime

def testYearlySalaryIncrement():
    print(employee.getSalary())
    employee.yearlySalaryIncrement()
    print(employee.getSalary())

def testNumberOfYears():
    print(employee.numberOfYears())

if __name__ == "__main__":
    employee = Employee(1, "Musa", "Manager", 100000, datetime(2020, 5, 17))
    testYearlySalaryIncrement()
    testNumberOfYears()
    