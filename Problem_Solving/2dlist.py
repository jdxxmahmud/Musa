lst = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
my_dict = {}

for i in range(0, len(lst)):
    my_dict[lst[i]] = len(lst[i])

print(my_dict)