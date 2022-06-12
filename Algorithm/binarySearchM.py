def Binary_Search(lst: int,key: int):
    high = len(lst)-1
    low = 0  
    while high >= low:
        mid = ( high + low ) // 2
        if key == lst[mid]:
            return mid 
        elif key > lst[mid]:
            low = mid + 1
        elif key < lst[mid]:
            high = mid - 1

    return -1 


array = list(range(77,87))
key = 24

key_index = Binary_Search(array, key)

print(key_index)