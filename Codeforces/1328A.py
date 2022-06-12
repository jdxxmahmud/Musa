# Problem Link: https://codeforces.com/problemset/problem/1328/A


t = int(input())
cases = []
for _ in range(t):
    a, b = list(map(int, input().split(' ')))
    # print(a, b)

    # Solution code goes here
    if not a % b:
        print(0)
    elif a < b:
        print(b-a)
    else:
        print((b * ((a//b) + 1) - a))
    ###
