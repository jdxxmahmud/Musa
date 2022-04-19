list1 = input("Enter you number: ")
list1 = list1.split(" ")
len_of_list = len(list1)

for i in range(1,len_of_list,2):
    print(list1[i])