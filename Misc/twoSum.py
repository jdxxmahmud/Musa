# In myList, find the pair that adds upto the variable
# target

myList = list(range(1, 100, 2))
print(myList)
target = 120
pairFound = False

for i in myList:
    if (target - i) in myList:
        print(i, target - i)
        pairFound = True
        break

if not pairFound:
    print(-1)
