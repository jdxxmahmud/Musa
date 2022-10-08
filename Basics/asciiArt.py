arr = [1, 2, 3, 4, 5]
lst = []

for i in range(0, len(arr)):
    Sublst = []
    for j in range(0, i+1):
        Sublst.append(arr[j])

    lst.append(Sublst)


print(lst)

    
    

        