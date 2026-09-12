"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True # There can't be any conflict on a free schedule

        intervals.sort(key=lambda item:item.start) # Sort by start time
        for i in range(1, len(intervals)):
             if intervals[i].start < intervals[i-1].end:
                 return False
        return True