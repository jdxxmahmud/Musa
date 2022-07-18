txt = input('')

lst = list(txt)

real_lst = []

for i in lst:
    if i not in real_lst:
        real_lst.append(i)


if len(real_lst) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

    