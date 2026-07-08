class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l < r:
            m = l + (r -l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        res = binary_search(0, pivot-1)
        if res != -1:
            return res

        return binary_search(pivot, len(nums)- 1)
