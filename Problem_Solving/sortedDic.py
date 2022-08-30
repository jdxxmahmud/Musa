dic = {'Chocolate':100,
        'Banana':120,
        'Apple':80
}
sortdic = {}
print(dic)

for k, v in sorted(dic.items()):
    sortdic[k] = v


print(sortdic)