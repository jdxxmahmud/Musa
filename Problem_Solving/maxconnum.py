arr = [1, 2, 11, 0, 0, 4]
num = 15
first = 0 
second = len(arr)
def maxSubarr(arr: int, num: int):
    while second >= first:
        val = 0 
        for i in range(first, second):
            