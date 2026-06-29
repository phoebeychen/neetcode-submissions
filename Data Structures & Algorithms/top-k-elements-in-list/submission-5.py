class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        #freq = [0] * len(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in map.items():
            freq[cnt].append(num)
        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res




            