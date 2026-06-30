class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        zero_cnt = 0
        prod = 1

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return res
        
        for i in range(len(nums)):
            if zero_cnt:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // nums[i]
        return res
