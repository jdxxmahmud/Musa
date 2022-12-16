def twoSum(arr, target):
    hi = len(arr)-1 
    lo = 0 

    while hi > lo:
        if arr[hi] + arr[lo] == target:
            return hi,lo
        elif arr[hi] + arr[lo] > target:
            hi -= 1
        else:
            lo += 1

    
lst = [1,3,4,5,6,8,9,11,13]
print(twoSum(lst,13))