from datetime import datetime

class Project:
    def __init__(self, name, endDate, stacks, teamMembers, budget, estimatedIncome, businessGoal, startDate = datetime.today(), revenue = None):
        self.name = name
        self.endDate = endDate
        self.stacks = stacks
        self.teamMembers = teamMembers
        self.budget = budget
        self.estimatedIncome = estimatedIncome 
        self.businessGoal  = businessGoal 
        self.startDate = startDate
        
        if revenue != None:
            self.revenue = revenue

    #METHODS

    def profitFromProject(self):
        return self.revenue - self.budget

    def allocateProfitFromProjectToEachTeamMember(self):
        tenPercentOfProfit = (self.revenue - self.budget)*0.10

        return tenPercentOfProfit/self.teamMembers



    #GETTER METHODS

    def getName(self):
        return self.name

    def getEndDate(self):
        return self.EndDate

    def getStacks(self):
        return self.stacks

    def getTeamMembers(self):
        return self.teamMembers

    def getBudget(self):
        return self.budget

    def getEstimatedIncome(self):
        return self.estimatedIncome

    def getBusinessGoal(self):
        return self.businessGoal
    
    def getStartDate(self):
        return self.startDate
    
    def getRevenue(self):
        return self.revenue

    #SETTER METHODS     

    def setName(self, name):
        self.name = name

    def setEndDate(self, endDate):
        self.endDate = endDate

    def setStacks(self, stacks):
        self.stacks = stacks

    def setTeamMember(self, teamMembers):
        self.teamMembers = teamMembers

    def setBudget(self, budget):
        self.budget = budget

    def setEstimatedIncome(self, estimatedIncome):
        self.estimatedIncome = estimatedIncome

    def setBusinessGoal(self, businessGoal):
        self.businessGoal = businessGoal 
        
    def setStartDate(self, startDate):
        self.startDate = startDate

    def setRevenue(self, revenue):
        self.revenue = revenue



