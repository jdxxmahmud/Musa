def pairfinder(arr, k):
    start = 0
    end = len(arr) - 1 
    pair = 0
    cone = 0 
    ctwo = 0 

    while start < end:
        if arr[start] + arr[end] == k:
            if arr[start] != arr[end]:
                for i in range(start, end+1):
                    if arr[i] == arr[start]:
                        cone +=1 
                    elif arr[i] == arr[end]:
                        ctwo += 1
                pair = pair + (cone*ctwo)
                cone = 0 
                ctwo = 0
            else:
                for i in range(start, end+1):
                    if arr[i] == arr[start]:
                        cone += 1
                        pair = pair + (((cone**2)-cone)/2)
                        cone = 0
        elif arr[start] + arr[end] > k:
            end -= 1 
        else:
            start += 1
        
    print(pair)

lst = [1,4,4,5,5,5,6,6,11]

pairfinder(lst,11)