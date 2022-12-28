def moveZeroes(nums):
        countZero = 0 # total zeroes
        index = 0     # position 
        for i in range(len(nums)): 
                if nums[i] == 0:
                        countZero += 1 # tracking the number of zeroes 
                else:
                        nums[index] = nums[i]
                        index += 1 # increasing for the next non-zero element 
        
        for i in range(len(nums)-countZero, len(nums)): # relpacing the zeroes at the end 
                nums[i] = 0

        return  nums

#test case
lst = [0, 1, 0, 3, 12]

print(moveZeroes(lst))







