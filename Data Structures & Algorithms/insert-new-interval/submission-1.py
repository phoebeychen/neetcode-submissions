class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # insert:
        intervals.insert(left, newInterval)

        # merge:
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        return res





        