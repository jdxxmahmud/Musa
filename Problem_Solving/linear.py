def linearSearch(arr: int, key: int):
    index = 0 
    for i in range(0, len(arr)):
        if arr[i] == key:
            return f'{i} is the index for key '
        
lst = [91, 93, 85, 83, 71, 77, 54, 51, 60, 69, 42, 48, 39, 33, 27, 
28, 19, 15, 10, 5, 8]

print(linearSearch(lst, 10))
