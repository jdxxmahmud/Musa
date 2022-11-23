def binarySearch(arr: int, key: int):
    hi = len(arr) - 1
    lo = 0 

    while lo < hi:
        mid = hi + lo // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1 
    return -1

arr = [1, 2, 3, 4, 5, 6]

print(binarySearch(arr, 4))

