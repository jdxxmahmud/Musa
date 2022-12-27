def arithmeticTriplets(nums: list, diff: int) -> int:
        dct = {}
        tpairs = 0
        while ...:
                for i in range(len(nums)-1, -1, -1):
                        if nums[i] - diff in nums:
                                if (nums[i] - diff) - diff in nums:
                                        dct['k'] = nums[i]
                                        dct['j'] = nums[i] - diff
                                        dct['i'] = nums[i] - (diff*2)
                                        tpairs +=  1

        print(tpairs)

        