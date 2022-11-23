def pairfinder(arr: int, key: int):

    counter = 0
    pointer = 0 

    while pointer < len(arr) - 1:
        for i in range(pointer+1, len(arr)):
            if arr[pointer] + arr[i] == key:
                counter += 1
            if arr[pointer] + arr[i] > key:
                break

        pointer += 1

    return counter

print(pairfinder([1, 4, 4, 5, 5, 5, 6, 6, 11], 11))