def checker(arr):
    for i in range(0, len(arr) // 2):
        if arr[i] != arr[len(arr)-1-i]:
            return False
    return True


arr = [1,2,1]
lst = [3, 4, 5]
print("Correct" if checker(arr)==True else 'Incorrect')
print("Correct" if checker(lst)==False else 'Incorrect')

 