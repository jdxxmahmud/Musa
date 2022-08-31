tpl = ((1, 3, 5, 7),(9, 10, 11, 13), (15, 17, 19, 21), (23, 25, 27, 29), (31, 33, 35, 37))
my_dict = {}

for i in range(0, len(tpl)):
    my_dict[tpl[i]] = len(tpl[i])


print(my_dict)