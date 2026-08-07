class Solution:
    def binary_search(self, nums:List[int], target:int) -> int:
        l = 0
        r = len(nums) - 1 
        ans = len(nums) # 初始化越界值，表示没找到

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                ans = mid # 记录当前位置，这可能是一个潜在的答案
                r = mid - 1
            else:
                l = mid + 1
        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        start = self.binary_search(nums, target)

        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = self.binary_search(nums, target + 1) - 1
        return [start, end]