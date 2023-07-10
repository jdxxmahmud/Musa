from datetime import date
from employee import Employee
from company import Company
employee1 = Employee('2021E', 'Musa', "coder", date(2021,6,9), 10 )

print(employee1.numberOfYears())