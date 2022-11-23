def merge(nums1: int, m: int, nums2: int, n: int):
    pointer = m + n - 1 
    first = m - 1
    second = n - 1
    
    while second > -1:
        if first == -1:
            for i in range(second+1):
                nums1[i] = nums2[i]
            break 
        if nums2[second] >= nums1[first]:
            nums1[pointer] = nums2[second]
            second -= 1
        else:
            nums1[pointer] = nums1[first]
            first -= 1

        pointer -= 1
        
    return nums1

nums1 = [10, 11, 13, 14, 15, 66, 77, 888, 999, 1233, 0, 0]
nums2 = [12,51]

print(merge(nums1, 10, nums2, 2))

