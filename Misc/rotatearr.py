def rotateSearch(arr: list):
    hi = len(arr) - 1
    lo = 0 
    val = hi 
    
    while hi >= lo:
        mid = (hi + lo) // 2 
        if arr[mid] > arr[val]:
            val = mid 
        elif arr[mid] > arr[lo]:
            lo = mid + 1
        else:
            hi = mid - 1

    return val  

arrOne = [1,2,3,4,5,6,7,8,9]
arrTwo = [2,3,4,5,6,7,8,9,1]
arrThree = [3,4,5,6,7,8,9,1,2]
arrFour = [4,5,6,7,8,9,1,2,3]
arrFive = [5,6,7,8,9,1,2,3,4]
arrSix = [6,7,8,9,1,2,3,4,5]
arrSeven = [7,8,9,1,2,3,4,5,6]
arrEight = [8,9,1,2,3,4,5,6,7]
arrNine = [9,1,2,3,4,5,6,7,8]

print(rotateSearch(arrOne))
print(rotateSearch(arrTwo))
print(rotateSearch(arrThree))
print(rotateSearch(arrFour))
print(rotateSearch(arrFive))
print(rotateSearch(arrSix))
print(rotateSearch(arrSeven))
print(rotateSearch(arrEight))
print(rotateSearch(arrNine))