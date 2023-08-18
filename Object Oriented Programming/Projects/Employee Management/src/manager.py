# example of inheritance

from employee import Employee
from datetime import datetime

class Manager(Employee):
    
    allocatedProjects = []
    def __init__(self, name, salary, position = "Manager", joiningDate = datetime.today()):
        from company import Company
        self.id = Company.getEmployeeId
        self.name = name 
        self.position = position
        self.salary = salary
        self.joiningDate = joiningDate

    def addProject(self, projectList):
        self.allocatedProject.extend(projectList)

