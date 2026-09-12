class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]

        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda item: item[0])
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            curr, prev = intervals[i], merged[-1]
            if curr[0] <= prev[1]: # If current start time is less than prev end time or prev start time
                merged[-1] = [prev[0], max(curr[1], prev[1])] # Extend duration
            else:
                merged.append(curr)
        return merged