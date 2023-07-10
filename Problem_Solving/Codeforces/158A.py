n, k = map(int, input("").split())

num = list(map(int, input().split()))

val = 0

for i in range(n):
    if num[i] >= num[k - 1] and num[i] != 0:
        val += 1

print(val)