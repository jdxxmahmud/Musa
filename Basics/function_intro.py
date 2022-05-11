# Function
# Functions are used so that we do not have to write the
# same code many times.


def sum(a: int, b: int):
    ans = a + b
    print("This function is amazing")
    print(f"the sum is {b} + {a} = {ans}")
    return a + b

## subtraction, power, division, multiplication


def main():
    print(sum(2, 5))
    print(sum(5, 11))

# String: I will give you my first name and second name separately,
# Your function will return the complete name, with the first letters
# capitalized


main()
