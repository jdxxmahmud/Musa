# this file contains the concept of inheritane, polymorphism, overiding and overloading 
import math

class polygons:
    def __init__(self, shape, sides, symmetry, rotationalsymmetry, length):
        self.shape = shape 
        self.symmetry = symmetry
        self.rotationalsymmetry = rotationalsymmetry
        self.length = length

    def printDescription(self):
        return(f'This polygon has {self.sides} and a length of {self.length} each')

class triangle(polygons):
    shape = 'triangle'
    sides = 3
    symmetry = 3
    rotationalsymmetry = 3
    def __init__(self, length):
        super().__init__(self.shape, self.sides, self.symmetry, self.rotationalsymmetry, length)

    def getArea(self, length = None):
        if length != None:
            return (math.sin(math.pi/3)*0.5*(length**2))
        return (math.sin(math.pi/3)*0.5*(self.length**2))

class square(polygons):
    shape = 'square'
    sides = 4
    symmetry = 4 
    rotationalsymmetry = 4 
    def __init__(self, length):
        super().__init__(self.shape, self.sides, self.symmetry, self.rotationalsymmetry, length)

    def getArea(self, length = None):
        if length != None:
            return length**2
        return self.length**2




box1 = triangle(5)
box2 = square(10)

print(box1.getArea())
print(box2.getArea(20))

print("No Error")

