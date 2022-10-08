def GCF(numOne: int, numTwo :int):

    dividend = max(numOne, numTwo)

    divisor = min(numOne, numTwo)

    while dividend % divisor != 0:
        temp = divisor
        divisor = dividend % divisor
        dividend = temp

    return divisor


print(GCF(16,24))