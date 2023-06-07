#changing letters until spaces come up 
#Space came up from left side (left pointer +=1 && space add to newstr)
#Space came up from right side (right pointer -= 1)musa is a good boy 
#Space comes up on both side
def reverse(txt):
    lo = 0
    hi = len(txt) - 1 
    txt = list(txt.lower())
    while lo <= hi:
        if txt[lo] != ' ' and txt[hi] != ' ':
            temp = txt[lo]
            txt[lo] = txt[hi]
            txt[hi] = temp
            hi -=1 
            lo +=1
        elif txt[lo] != " " and txt[hi] == " ":
            hi -= 1
        elif txt[lo] == " " and txt[hi] == " ":
            lo += 1 
            hi -= 1
        else:
            lo += 1
    newtxt = ''
    for i in txt:
        newtxt = newtxt + i 

    return newtxt

print((reverse("Musa is a good boy")))