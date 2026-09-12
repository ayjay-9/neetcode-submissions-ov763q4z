class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            if newInterval:
                return[newInterval]
            else:
                return [[]]

        intervals.append(newInterval)
        intervals.sort(key=lambda item:item[0]) # sort by start time
        added = [intervals[0]]

        for i in range(1, len(intervals)):
            prev, curr = added[-1], intervals[i]
            if curr[0] <= prev[1]:
                added[-1] = [prev[0], max(curr[1], prev[1])]
            else:
                added.append(curr)

        return added