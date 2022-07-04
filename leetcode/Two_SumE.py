def twoSum(nums: list[int], key: int):
    
    dct = {}

    for i in range(len(nums)):

        dct[nums[i]] = i 

    nums.sort()

    lo = 0
    hi = len(nums) - 1

    while lo < hi :
        val = nums[lo] + nums[hi]
        
        if val == key:
            return [dct[nums[lo]],dct[nums[hi]]]
        
        if val > key:
            hi -= 1

        elif val < key:
            lo += 1 

lst = [1, 2, 3, 4, 7, 8, 9, 10, 5, 6]
key = 11

print(twoSum(lst, key))
    
    