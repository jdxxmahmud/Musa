lst = [9]
lst[-1] = lst[-1] + 1
print(lst)
print(str(lst))

txt = ''

for i in lst:
    txt = txt + str(i)

print(txt)

print(list(txt))

txt = list(txt)

for i in range(0, len(txt)):
    txt[i] = int(txt[i])

print(txt)