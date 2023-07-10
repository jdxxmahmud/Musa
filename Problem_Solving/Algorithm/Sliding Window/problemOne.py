# Problem Statement - Given an integer array, find the minimum sum subarray of size k, where k is a positive integer.

def minSum(arr, k):
    if k == 1:
        return min(arr)
    pointer = 0
    res = 99999999
    reslst = [0, 0]
    for i in range(k, len(arr)):
        counter = 0
        for n in range(pointer, i):
            counter += arr[n]  
        if counter < res:
            res = counter
            reslst[0] = pointer
            reslst[1] = k - 1
        pointer += 1

    print(res)
    return reslst

        


## test[0] -> arr ; test[1] -> k ; test[2] -> result
testone = [[10,4,2,5,6,3,8,1], 3, [1,3]]
testtwo = [[1,9,2,8,3,7,4,6,5], 4, [0,3]]
testthree = [[9,8,7,6,5,3,4,1,2], 1, [7]]

print(minSum([10,4,2,5,6,3,8,1], 3))

