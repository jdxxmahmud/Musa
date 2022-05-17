def GCF(x:int, y:int):
    
    rem = 0
    
    if x == y :
        return x
    
    if x < y :
        r = y % x
        y = x
        x = r
        while x != 0:
            r = y % x 
            y = x
            x = r
        return y

    else:
        r = x % y
        x = y
        y = r
        while y != 0:
            r = x % y
            x = y
            y = r
        return x

GCF(10,5)