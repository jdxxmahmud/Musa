#input is the first line. output is the second line. basically reverse the string. But we can't use [::-1]

def Reverse(txt):
    newtxt_ =   ''
    for i in range(len(txt)-1, -1, -1):
        newtxt_ = newtxt_ + txt[i]

    return newtxt_

print(Reverse('musa is a good boy'))
