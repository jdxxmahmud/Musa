nums = input()
ans = "+".join(map(str, sorted(map(int, nums.split("+")))))
print(ans)