import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. 定位左侧重叠边界 (i)
        # 目标：找到第一个结束时间 >= newInterval.start 的区间索引
        # 也就是第一个可能与新区间发生重叠的区间
        # 提示：[x[1] for x in intervals] 在实际面试中可以用 bisect_left 自定义 key
        ends = [x[1] for x in intervals]
        i = bisect.bisect_left(ends, newInterval[0])
        
        # 2. 定位右侧重叠边界 (j)
        # 目标：找到第一个开始时间 > newInterval.end 的区间索引
        # 也就是第一个完全在新区间之后的区间
        starts = [x[0] for x in intervals]
        j = bisect.bisect_right(starts, newInterval[1])
        
        # 3. 合并受影响的区间
        # 如果 i == j，说明 newInterval 与现有区间没有任何重叠，直接插入在 i 位置即可
        # 如果 i < j，说明索引 i 到 j-1 的区间都需要被合并
        if i < j:
            # 合并后的起点：取 newInterval 和第一个重叠区间起点的最小值
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # 合并后的终点：取 newInterval 和最后一个重叠区间终点的最大值
            newInterval[1] = max(newInterval[1], intervals[j-1][1])
            
        # 4. 利用切片重组结果
        # [无重叠的左侧部分] + [合并后的新区间] + [无重叠的右侧部分]
        return intervals[:i] + [newInterval] + intervals[j:]