text = input("Enter your list here: ")
lst = text.split(" ")
lenlst = len(lst)
print(lst)

for i in range(0,lenlst):
    lst[i] = int(lst[i])


print(lst)

odd = []
even = []
for i in range(0,lenlst):
    if lst[i] % 2 == 0 :
        odd.append(lst[i])
    else:
        even.append(lst[i])
 

print(f"odd:{odd} \t even:{even}")
