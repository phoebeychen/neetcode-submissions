class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            width = r - l
            area = width * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] <= height[r]:
                l += 1
            else: # 使用两个独立的 if 语句可能会导致同一次循环中左右指针同时移动
                r -= 1
        return maxArea