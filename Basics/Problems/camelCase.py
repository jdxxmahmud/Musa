### Convert a string into camelcase string

### Input: "My name is musa"
### Output: "My NaMe Is MuSa"


import string


def camelCase(str: string):
    # Your code starts here
    ans = str[0].upper()
    prevCapital = True
    lenstr = len(str)

    for i in range(1, lenstr):
        if str[i] != " ":
            if prevCapital == True:

                ans = ans + str[i].lower()
                prevCapital = False

            else:
                
                ans = ans +str[i].upper()
                prevCapital = True
                
        else:
            ans = ans + str[i]

    print(ans)

    return ans
    # Your code ends here


### Do not edit anything after this line ###
print("Test Case Passed" if camelCase("I am in Bangladesh") == "I aM iN bAnGlAdEsH" else "Test Failed")
print("Test Case Passed" if camelCase("You and me are doing codes") == "YoU aNd Me ArE dOiNg CoDeS" else "Test Failed")
print("Test Case Passed" if camelCase("My name is musa") == "My NaMe Is MuSa" else "Test Failed")



