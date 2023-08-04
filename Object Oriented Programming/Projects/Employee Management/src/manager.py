# example of inheritance

from employee import Employee
from datetime import datetime

class Manager(Employee):
    
    allocatedProjects = []
    def __init__(self, id, name, salary, position = "Manager", joiningDate = datetime.today()):
        self.id = id
        self.name = name 
        self.position = position
        self.salary = salary
        self.joiningDate = joiningDate

    def addProject(self, projectList):
        self.allocatedProject.extend(projectList)

