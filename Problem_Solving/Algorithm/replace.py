 def interpret(s: str,d):
    tmp= ""
    res=""
    for i in range(len(s)):
        tmp+=s[i]
        if(tmp in d):
            res+=d[tmp]
            tmp=""
    return print(res)

d = {"(al)":"al", "()":"o","G":"G"}

interpret("G()(al)",d)


