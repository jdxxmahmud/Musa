nums = list(map(int, input().split("+")))
nums = sorted(nums)

val  = str(nums[0])

for i in range(1, len(nums)):
    val = val + "+" + str(nums[i]) 

print(val)