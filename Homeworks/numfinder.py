#Find the input number's index from the list given.
# Input:
        #list : 12345
        #input number : 4
# # Output: 3


lst = input("Enter your list: ")

lst = lst.split(" ")

lenlst = len(lst)

for i in range(0, lenlst):
    lst[i] = int(lst[i])

num = int(input("Number: "))

for i in range(0, lenlst):
    if lst[i] == num :
        print(i)
