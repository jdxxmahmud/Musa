def twoSum (lst , target): 

    for i in lst:
        if target - i in lst:
            return i, target - i

    return -1 


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 12

val = twoSum(lst, target)
print(type(val))

target = 29

print(twoSum(lst, target))


