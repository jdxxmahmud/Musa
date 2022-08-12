class Fruits:

    def __init__(self, name_, fruitID_, quantity_, costPrice_, sellingPrice_): 
        
        #Public
        self.name = name_ 
        self.fruitID = fruitID_
        self.quantity = quantity_

        #Private 
        self.__costPrice = costPrice_
        self.__sellingPrice = sellingPrice_ 

    #Getter methods
    def get_costPrice(self):
        return self.__costPrice
    
    def get_sellingPrice(self):
        return self.__sellingPrice

    #Setter methods 
    def set_costPrice(self, costPrice_):
        self.__costPrice = costPrice_

    def set_sellingPrice(self, sellingPrice_):
        self.__sellingPrice = sellingPrice_
    
    #Processing methods
    def calculate_profit(self):
        return self.__sellingPrice - self.__costPrice

    def calculate_totalProfit(self):
        return self.quantity * (self.__sellingPrice - self.__costPrice)

def fruitInput():

    x_name = input("Enter fruit name: ")
    x_fruitID = input("Enter fruitID: ")
    x_quantity = int(input("Enter quantity:"))
    x_costPrice = int(input("Enter cost price: "))
    x_sellingPrice = int(input("Enter selling price: "))
    print()

    return Fruits(x_name, x_fruitID, x_quantity, x_costPrice, x_sellingPrice)

def fruitPrinter(arr):

    for i in arr:
        print(i.name, end = ", ")
        print(i.fruitID, end = ", ")
        print(i.calculate_profit(), end = ", ")
        print(i.calculate_totalProfit())

# fruit1 = fruitInput()

# print(fruit1.name, end = ", ")
# print(fruit1.fruitID, end = ", ")
# print(fruit1.quantity, end = ", ")
# print(fruit1.get_costPrice(), end = ", ")
# print(fruit1.get_sellingPrice())

fruit_list = []

n = int(input("Type of fruits: "))

for i in range(n):
    newFruit = fruitInput()

    fruit_list.append(newFruit)

fruitPrinter(fruit_list)
