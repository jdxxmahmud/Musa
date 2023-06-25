class Animal:

    def __init__(self, legs_, tail_, colour_):

        #Public Attributes
        self.legs = legs_
        self.tail = tail_

        #Private Attributes 
        self.__colour = colour_

    #Getter Methods
    def get_colour(self):
        return self.__colour
        
    def get_legs(self):
        return self.legs

    def get_tail(self):
        return self.tail

    #Setter Methods 
    def set_colour(self, colour_):
        self.colour = colour_

    def set_legs(self, legs_):
        self.legs = legs_

    def set_tail(self, tail_):
        Sself.tail = tail_
    
        
        


#Objects
cat = Animal(4, True, "Black")

print(cat.get_colour())