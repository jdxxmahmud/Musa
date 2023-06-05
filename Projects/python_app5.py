def search(arr, key):
    hi = arr[-1]
    lo = 0
    
    while hi >= lo:
        mid = (hi + lo) // 2 
        if arr[mid] == key:
            return mid 
        elif arr[mid] > key:
            hi = mid - 1 
        else:
            lo = mid + 1
        return -1 

lst = [1,2,3,4,5,6,7,8]
key = 5

print(search(lst, key))
            
        