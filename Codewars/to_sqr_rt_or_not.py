# Problem Link: https://www.codewars.com/kata/57f6ad55cca6e045d2000627
# Problem Name: To square(root) or not to square(root)
from math import sqrt

def square_or_square_root(arr):
    list1 = arr
    len1 = len(list1)
    for i in range(0, len1):
        if sqrt(list1[i]) == int(sqrt(list1[i])):
            list1[i] = sqrt(list1[i])
        else:
            list1[i] = list1[i] ** 2
    return list1



arr = [4, 3, 9, 7, 2, 1]
ans = square_or_square_root(arr)
result = [2, 9, 3, 49, 4, 1]
print("Accepted" if result == ans else "Not Accepted")
