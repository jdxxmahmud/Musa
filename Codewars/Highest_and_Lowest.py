
#link - https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

numbers = "1 2 3 4 5 6 7 8"

    numbers = numbers.split(" ")

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])

    print(numbers)