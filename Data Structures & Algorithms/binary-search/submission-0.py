class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:

            mid = l + (r - l) // 2 # mid 要随循环l和r的更新而更新

            if nums[mid] > target: # target -> nums[l] + nums[r]
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1