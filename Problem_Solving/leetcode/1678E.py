'''
def GPI(command: str):
    val = ''
    lst = list(command)
    for i in (0,len(lst)):
        if lst[i] == 'G':
            val = val + 'G'
        elif lst[i] == '(' and lst[i+1] == ')':
            val = val + 'o'
        elif lst[i] == '(' and lst[i+1] == 'a':
            val = val + 'al'

    return print(val)


txt = "()G(al)"

GPI(txt)
'''

