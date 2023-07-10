def twoSum(arr, key):
    lo = 0 
    hi = len(arr) - 1
    while hi >= lo:
        if arr[lo] + arr[hi] == key:
            return f'{arr[lo]} and {arr[hi]} are a pair that adds up to {key}'
        elif arr[lo] + arr[hi] > key:
            hi -= 1
        else:
            lo += 1 

print(twoSum([-5, -2, 0, 1, 10], 11))
        