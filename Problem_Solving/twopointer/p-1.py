def pairfinder(arr: int, key: int):
    counter = 0
    first = 0
    second = len(arr) - 1
    c_one = 0
    c_two = 0
    
    while first < second:
        if arr[first] + arr[second] > key:
            second -= 1
        elif arr[first] + arr[second] < key:
            first += 1
        elif arr[first] + arr[second] == key:
            for i in arr:
                if i == arr[first]:
                    c_one += 1
                if i == arr[second]:
                    c_two += 1
            counter += (c_one * c_two)
            break 

    
    return counter

print(pairfinder([1, 4, 4, 5, 5, 5, 6, 6, 11], 11))