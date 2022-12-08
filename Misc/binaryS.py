def binarySearch(arr, key):

    hi = len(arr) -1 
    lo = 0 

    while hi >= lo:
        mid = (hi + lo) // 2 
        if key  == arr[mid]:
            return mid
        elif key > arr[mid]:
            lo = mid 
        elif key < arr[mid]:
            hi = mid 

    return -1 


arr = [5, 6, 7, 8, 9, 1, 2, 4]
 
print(binarySearch(arr, 5))

v = 12
val = len(list(str(v)))
print(val)