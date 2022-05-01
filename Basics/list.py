from time import sleep


my_list = input("Input the numbers: ").split(" ")
len_of_my_list = len(my_list)


# List: 65 35 74 90 81 72 35 18
for i in my_list:  # You can not update my_list using i
    print(i)

print("Using another loop \n\n\n")
sleep(3.5)

# You can change your list using this, basically
for i in range(0, len_of_my_list):  # You can update my_list using i
    my_list[i] = int(my_list[i])
    print(my_list[i])

    

"""
    my_list[i] = int(my_list[i])
    print(my_list[i])
"""