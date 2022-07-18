# 1

'''
Assume that the variable data refers to the list [8, 9, 7, 2]. 
Here data = [8, 9, 7, 2]
Write the values of the following expresssions:

a. data[2]
val = 7
b. data[-2]
val = 7
c. data[0:2]
val = [8, 9]
d. data + [7, 9, 8]
val = 24


Note: You can not run the code for this question
'''

# 2

'''
Store the result of question 1(d) in a variable called arr.
Now write a code that shows whether the variable arr is a pallindrome or not.
Return True if pallindrome, False if not.
Pallindrome: If you reverse a list, you get the same order of variables.
Examples: For [1, 2, 1] if you reverse this, you get [1, 2, 1]
          so, this is a pallindrome list
[1, 2, 3] is not pallindrome, since you get [3, 2, 1] if reversed
'''


def isPallindrome(arr):
    lst = []
    for i in range(len(arr)-1, -1, -1):
        lst.append(arr[i])

    if lst == arr:
        return True
    else:
        return False
        


print("Correct" if isPallindrome([1, 2, 1]) == True else "Incorrect")
print("Correct" if isPallindrome([1, 2, 3]) == False else "Incorrect")
data = [8, 9, 7, 2]
