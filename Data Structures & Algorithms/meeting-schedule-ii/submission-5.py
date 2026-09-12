"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 # There can't be any conflict on a free schedule

        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res