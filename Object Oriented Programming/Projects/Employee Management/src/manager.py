# example of inheritance

from employee import Employee
from datetime import datetime

class Manager(Employee):
        
    def __init__(self, id, name, salary, position = "Manager", joiningDate = datetime.today()):
        self.id = id
        self.name = name 
        self.salary = salary
        self.position = position
        self.joiningDate = joiningDate
        self.allocatedProjects = []


    def addProjects(self, projectList):
        self.allocatedProject.extend(projectList)

