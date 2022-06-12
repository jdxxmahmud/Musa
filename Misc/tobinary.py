def tobinary(x: int):
    quo = x

    rem  = 0 

    val = ""

    while quo != 0 :

        rem = str(quo % 2)

        quo = int(quo / 2)

        val = rem + val 

    return val 


print(tobinary(100))