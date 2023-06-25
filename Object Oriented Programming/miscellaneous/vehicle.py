class Vechicle:
    def __init__(self, wheels_, seats_, maxPassenger_, roof_):
        #attributes - Public
        self.__wheels = wheels_
        self.seats = seats_
        self.maxPassenger = maxPassenger_
        self.roof = roof_

        #attributes - Private
        self.__illegal = -1
        
    #getter method
    def get_wheels(self):
        return self.wheels

    def get_illegal(self):
        return self.__illegal
    
    def get_seats(self):
        return self.seats

    def get_maxPassenger(self):
        return self.maxPassenger

    def get_roof(self):
        return self.roof

    #setter method
    def set_wheel(self, wheels_):
        self.wheels = wheels_
    
    def set_illegal(self, illegal_):
        self.__illegal = illegal_
        
    def set_seats(self, seats_):
        self.seats = seats_
    
    
car = Vechicle(4, 4, 5, True)
bike = Vechicle(2, 2, 2, False)
rickshaw = Vechicle(2, 2, 2, False)
truck = Vechicle(6, 3, 30, True)
print(car.get_illegal())

rickshaw.__wheels = 2