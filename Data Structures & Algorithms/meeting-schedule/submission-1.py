"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        n = len(intervals)

        intervals.sort(key=lambda i: i.start) # lambda sorting不会写

        for i in range(1,n):
            A = intervals[i - 1]
            B = intervals[i]
            
            if A.end > B.start:
                return False
        return True