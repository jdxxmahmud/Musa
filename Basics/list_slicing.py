# List slicing

from os import sep


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
len_list = len(my_list)

slice1 = my_list[2:10]  # same as [2:10:1]
slice2 = my_list[2:10:2]

slice3 = my_list[:10]  # Will start from 0 index
slice4 = my_list[4:]   # Will continue upto the end

slice5 = my_list[::-1]   # Will print the list reversely

slice6 = my_list[4:9:-1]
# my_list[4:9] = [5, 6, 7, 8]
# for step = -1   => index will go backward
# hence the output will be blank

slice7 = my_list[-4:-9:-1]
# my_list[-4:-9] = [9, 8, 7, 6, 5]
# for step = -1 => index will go backward
# so, output will be [9, 8, 7, 6, 5]


slice8 = my_list[-4: -9: 1]
#

text = "musa sudad"

for i in my_list[9:4:-1]:
    print(i)

print(text.title())
