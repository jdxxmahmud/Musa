# In myList, find the pair that adds upto the variable
# target

myList = [-1, 2, 3, 4, 8, 10, 12, 18]
target = 13
pairFound = False

for i in myList:
    if (target - i) in myList:
        print(i, target - i)
        pairFound = True
        break

if not pairFound:
    print(-1)
