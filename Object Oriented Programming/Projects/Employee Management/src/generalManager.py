from employee import Employee
from datetime import datetime

class GeneralManager(Employee):
    
    def __init__(self, id, name, salary, position = "General Manager", joiningDate = datetime.today()):
        self.id = id
        self.name = name 
        self.salary = salary
        self.position = position
        self.joiningDate = joiningDate
