def dic_maker(arr):
    arr = sorted(arr)
    dic = {}

    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # for key, val in dic.items():
    #     print(key, end = " ")
    #     print(val, end = " ")
    #     print(dic[key + 1])

    lst = list(dic.items())

    for i in range(len(lst)):
        for j in range(0, len(lst) - i -1):
            if lst[j][0] > lst[j+1][0]:
                current = lst[j][0]
                lst[j][0] = lst[j+1][0]
                lst[j+1][0] = current

    lst = dict(lst)

    print(lst)

      



arr = [ 1, 2, 3, 9, 2, 10, 12, 4, 3, 1, 2, 2, 11, 10, 9]

dic_maker(arr)

