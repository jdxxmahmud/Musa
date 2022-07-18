# 1

'''
Assume that te variable data refers to the list [8, 9, 7]. 
Here data = [8, 9, 7, 2]
Write the values of the following expresssions:

a. data[2]
b. data[-2]
c. data[0:2]
d. data + [7, 9, 8]

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
    # Your code goes here


print("Correct" if isPallindrome([1, 2, 1]) == True else "Incorrect")
print("Correct" if isPallidrome([1, 2, 3]) == False else "Incorrect")
