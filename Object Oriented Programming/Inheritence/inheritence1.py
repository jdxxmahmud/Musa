'''
vehicle
    tires
    engine  
    Windows
    steering

    
car
    ..
    gear
    windshield

cycle
    ..
    chain

plane
    ..
    wings
    back
    washroom

'''

class Vehicle:
    def __init__(self, name, tires, engines, windows) -> None:
        self.name = name
        self.tires = tires
        self.engines = engines
        self.windows = windows

    def printDescription(self):
        # print(f'This {self.name} has {self.tires} tires')
        pass

    def calculateTotalEnergyOfTheEngine(self, engineNumber, HP):
        print(f'This {self.name} has {engineNumber} engines and energy is {HP * engineNumber}')


class Car(Vehicle):
    name = "Car"
    engineNumber = 4
    def __init__(self, tires, engines, windows) -> None:
        super().__init__(self.name, tires, engines, windows)

    def calculateTotalEnergyOfTheEngine(self, HP):
        print("This car has energer", HP)


    


myCar = Car( 4, "Yes", 6)
myCar.printDescription()
myCar.calculateTotalEnergyOfTheEngine(750)
