list1 = input("Enter you numbers: ")
list1 = list1.split(" ")
len_1 = len(list1)

for i in range(0, len_1):
    list1[i] = int(list1[i])

even = []
odd = []

for i in list1 : 
    if i % 2 == 0 :
        even.append(i)
    else :
        odd.append(i)

print (even)

print (odd)
