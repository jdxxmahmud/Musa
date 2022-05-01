import string


def camelCase(str: string):
    # Your code starts here
    ans = ""
    lstr = len(str)
    for i in range(0,lstr):
        if str[i] != " ":
            if str[i] == str[i].upper():
                ans = ans + str[i].lower()
            elif str[i] == str[i].lower():
                ans = ans + str[i].upper()
        else:
            ans = ans + str[i]
    print(ans)
    return ans
    # Your code ends here


### Do not edit anything after this line ###
print("Test Case Passed" if camelCase("I am in Bangladesh") == "I aM In BaNgLaDeSh" else "Test Failed")
print("Test Case Passed" if camelCase("You and me are doing codes") == "YoU AnD mE aRe DoInG cOdEs" else "Test Failed")


