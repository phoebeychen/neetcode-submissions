from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = Counter(nums)

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j-1>i and nums[j-1] == nums[j]:
                    continue
                target = -(nums[i]+nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])

            for j in range(i+1, len(nums)): # 确保i能循环到每个数字
                count[nums[j]] += 1
        return res
                
                

            

        