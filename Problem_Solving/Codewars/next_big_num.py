nums = list(input(''))

for i in range(0, len(nums)):

    nums[i] = int(nums[i])

upper = 0
lower = 0

for i in range(1, len(nums)):
    for n in range(0, len(nums) - 1):
        if nums[i] < nums[n]:
            upper = nums[n]
            lower = nums[i]



val = str(upper) +' '+str(lower) 


print(val)
