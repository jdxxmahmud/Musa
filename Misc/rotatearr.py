arr = [1,2,3,4,5,6,7]
arr = arr[3*-1:len(arr)] + arr[0:(3-1)*-1]
print(arr)
