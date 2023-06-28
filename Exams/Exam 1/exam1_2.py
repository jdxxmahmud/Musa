
'''
Explain the following code

for input
5
3
ABA
11
DDBBCCCBBEZ
7
FFGZZZY
1
Z
2
AB

'''


def isSuspicious(tasks, n):
    checker = []
    for _ in range[26]:
        checker.append([0, 0])

    checker[ord(tasks[0]) - ord('A')][0] == 1
    for i in range(1, n):
        if checker[ord(tasks[i]) - ord('A')][1]:
            return "NO"
        checker[ord(tasks[i]) - ord('A')][0] = 1
        if tasks[i - 1] != tasks[i]:
            checker[ord(tasks[i - 1]) - ord('A')][1] = 1

    return "YES"


t = int(input())
while t:
    t -= 1
    n = int(input())
    tasks = input()

    print(isSuspicious(tasks, n))


