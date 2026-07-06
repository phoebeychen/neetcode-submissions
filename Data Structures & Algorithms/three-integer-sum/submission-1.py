class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        # sortedNUms = [-4,-1,-1,0,1,2]
        nums.sort() # 不占据额外空间
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # 去重一般判断第二个
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else: 
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return res