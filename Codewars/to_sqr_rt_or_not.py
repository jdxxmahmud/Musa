# Problem Link: https://www.codewars.com/kata/57f6ad55cca6e045d2000627
# Problem Name: To square(root) or not to square(root)
from math import sqrt


def square_or_square_root(arr):
    len_list = len(arr)
    for i in range(len_list):
        if sqrt(arr[i]) == int(sqrt(arr[i])):
            arr[i] = sqrt(arr[i])
        else:
            arr[i] = arr[i] ** 2
    return arr


arr = [4, 3, 9, 7, 2, 1]
ans = square_or_square_root(arr)
result = [2, 9, 3, 49, 4, 1]
print("Accepted" if result == ans else "Not Accepted")
