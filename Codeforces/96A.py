lst = input("")


def checker(lst: str):
    lst = list(lst)

    zero_flag = 0
    one_flag = 0

    for i in range(0, len(lst)-1):
        if lst[i] == lst[i+1] and lst[i] == '1':
            one_flag += 1
            if one_flag >= 7:
                return print("Yes")
            else:
                one_flag = 0

        if lst[i] == lst[i+1] and lst[i] == '0':
            zero_flag += 1
            if zero_flag >= 7:
                return print("Yes")
            else:
                zero_flag = 0


    return ("NO")


checker(lst)