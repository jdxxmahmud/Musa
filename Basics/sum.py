
'''

    => Take numbers input and store them in a list.
    Then convert the numbers into integers.
    The elements are: 15 20 10 30 5
    
    => Implement the sum() function on a list
    without using the sum() function
    
    => I will give you a list, find the sum 
    of the elements of the list, without using
    sum() function.
    [hint: You have to use loop]
'''
list1 = input("Enter you number: ")
list1 = list1.split(" ")
len_of_list = len(list1)

for i in range(len_of_list) :
    list1[i] = int(list1[i])

print(list1)

Total = 0 

for i in list1 :
    Total = Total + i  

print(f"Total {Total}")