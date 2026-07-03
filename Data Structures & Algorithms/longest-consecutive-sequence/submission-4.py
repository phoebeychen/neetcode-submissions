class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [-1, -1, 0, 1,3,4,5,6,7,8,9]
        
        if not nums:
            return 0

        curr = nums[0]
        streak = 0

        res = 0       
        nums.sort()
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i+= 1
            curr += 1
            streak += 1
            res = max(res, streak)
        return res
