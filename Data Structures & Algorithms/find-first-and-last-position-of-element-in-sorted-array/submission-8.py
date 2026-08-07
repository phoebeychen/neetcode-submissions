class Solution:
    def binary_search(self, nums:List[int], target:int) -> int:
        l = 0
        r = len(nums) - 1 

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        start = self.binary_search(nums, target)

        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = self.binary_search(nums, target + 1) - 1
        return [start, end]