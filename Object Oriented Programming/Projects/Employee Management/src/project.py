import datetime

class Project:
    def __init__(self, date, budget, estimatedIncome, businessGoal):
        self.date = date 
        self.budget = budget
        self.estimatedIncome = estimatedIncome 
        self.businessGoal  = businessGoal

    def getDate(self):
        return self.date
    
    def getBudget(self):
        return self.budget

    def getEstimatedIncome(self):
        return self.estimatedIncome

    def getBusinessGoal(self):
        return self.businessGoal

    def setDate(self, date):
        self.date = date

    def setBudget(self, budget):
        self.budget = budget

    def setEstimatedIncome(self, estimatedIncome):
        self.estimatedIncome = estimatedIncome

    def setBusinessGoal(self, businessGoal):
        self.businessGoal = businessGoal 
        
