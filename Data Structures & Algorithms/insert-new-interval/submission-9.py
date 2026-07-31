class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        # # merge:
        # res = []
        # for interval in intervals:
        #     if not res or interval[0] > res[-1][1]: # res[-1]表示列表中最后一个元素
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(interval[1], res[-1][1]) 
        # return res

        new_interval_idx = left
        start_val = newInterval[0]
        end_val = newInterval[1]
        
        merge_start_idx = new_interval_idx
        merge_end_idx = new_interval_idx
        
        while True:
            test_merge_start_idx = max(merge_start_idx - 1, 0)
            test_merge_end_idx = min(merge_end_idx + 1, len(intervals)-1)
            new_merge_start_idx = merge_start_idx
            new_merge_end_idx = merge_end_idx
            # If start_val <= end_val of prev interval, merge
            if start_val <= intervals[test_merge_start_idx][1]:
                new_merge_start_idx = test_merge_start_idx
            # If end_val >= start_val of next interval, merge
            if end_val >= intervals[test_merge_end_idx][0]:
                new_merge_end_idx = test_merge_end_idx
            
            # If We have a new Prev_Idx or a New Next_Idx, Continue
            if merge_start_idx > new_merge_start_idx or merge_end_idx < new_merge_end_idx:
                merge_start_idx = new_merge_start_idx
                merge_end_idx = new_merge_end_idx
            else:
                break
        print(intervals)
        new_start_val = min(intervals[merge_start_idx][0], intervals[merge_end_idx][0])
        new_end_val = max(intervals[merge_start_idx][1], intervals[merge_end_idx][1])
        print(merge_start_idx, merge_end_idx)
        print(new_start_val, new_end_val)
        intervals = intervals[0:merge_start_idx]+[[new_start_val, new_end_val]] + intervals[merge_end_idx+1:]
        return intervals


        