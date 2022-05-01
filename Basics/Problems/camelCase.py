### Convert a string into camelcase string

### Input: "My name is musa"
### Output: "My NaMe Is MuSa"


import string


def camelCase(str: string):
    # Your code starts here
    ans = str[0].upper()
    prevCapital = True
    lenstr = len(str)

    for i in range(1,lenstr):
        if str[i] != " ":
            if i % 2 == 0:
                ans = ans + str[i].lower()
            else:
                ans = ans +str[i].upper()
        else:
            ans = ans + str[i]
    return print(ans)
    # Your code ends here


### Do not edit anything after this line ###
print("Test Case Passed" if camelCase("I am in Bangladesh") == "I aM In BaNgLaDeSh" else "Test Failed")
print("Test Case Passed" if camelCase("You and me are doing codes") == "YoU AnD mE aRe DoInG cOdEs" else "Test Failed")



