### Convert a string into camelcase string

### Input: "My name is musa"
### Output: "My NaMe Is MuSa"


import string


def camelCase(str: string):
    pass


def main():
    print("Test Case Passed" if camelCase("I am in Bangladesh") == "I aM In BaNgLaDeSh" else "Test Failed")
    print("Test Case Passed" if camelCase("You and me are doing codes") == "YoU AnD mE aRe DoInG cOdEs" else "Test Failed")

if __name__ == "main":
    main()

