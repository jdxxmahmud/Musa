'''
problem link: https://www.codewars.com/kata/622de76d28bf330057cd6af8
'''




'''

1-9 = 9 numbers || 9 * 1 digits  || last number 9
10-99 = 90 numbers || 90 * 2 digits || last number 99
100 - 999 = 900 numbers || 900 * 3 digits || last number 999
1000 - 9999 = 9000 numbers || 9000 * 4 digits || last number 9999
10000 - 99999 = 90000 || 90000 * 5 || last number 99999

'''

summary = 346
pagelist = []
for i in range(1, summary + 1):
    pagelist.append(str(i))
    print(pagelist)
    if len(str(i)) == 2:
        i += 1
    if len(str(i)) == 3:
        i += 2
me = "".join(pagelist)  
print(me[-3:])