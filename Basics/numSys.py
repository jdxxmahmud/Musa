def converter(num: int, base: int):

    quo = num
    val = ''  

    while quo != 0:

        val = str(quo % base) + val

        quo = quo // base

    return val

        
    
print(converter(9,5))

