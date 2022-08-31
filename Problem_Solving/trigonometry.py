AB = int(input(""))
def Shaded_area(AB: int):
    # for square 1/2d^2 = area 
    square = 1/2 * (AB**2)

    # for circle pi*d/2^2
    circle = 3.142 * (AB/2)**2

    shaded_area = circle - square 

    return print(shaded_area)

Shaded_area(AB)