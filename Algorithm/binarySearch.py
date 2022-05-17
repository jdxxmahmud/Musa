## You will be given a sorted list/array
## ascending, normally
## you'll be given a key, just like linear search

## Why binary search, if we already have linear search.
## Linear search is slow.

## 

def bin_search(my_list: int, key: int):
    hi = len(my_list) - 1
    lo = 0
    
    while(hi >= lo):
        mid = (hi + lo)//2
        if key == my_list[mid]:
            return mid
        elif key > my_list[mid]:
            lo = mid + 1
        elif key < my_list[mid]:
            hi = mid - 1
                
    return -1


my_list = [1, 5, 6, 7, 12, 10, 120, 130, 2000]
key = 120

ans = bin_search(my_list, key)
print(f"position of {key} in the list is {ans}" 
      if ans > -1 
      else "Not found")
