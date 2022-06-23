# Problem Link: https://codeforces.com/problemset/problem/1328/A


t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split(' ')))
    # print(a, b)

    if a % b == 0:
        print(0)
    elif a < b:
        print(b-a)
    else:
        print(b * ((a//b) + 1) - a)
