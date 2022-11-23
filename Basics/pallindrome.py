def isPallindrome(x :int):
    x = str(x)
    if x == x[::-2]: 
        return True
    else:
        return False

print(isPallindrome(202))








