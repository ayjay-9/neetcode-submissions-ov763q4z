from math import floor, ceil

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Median = ceil((N+1) / 2)th position
        combined_array = nums1
        combined_array += [num for num in nums2]
        combined_array = sorted(combined_array)
        l, r = 0, len(combined_array)-1
        size, pos, median = r+1, (l+r) / 2, 0
        if pos.is_integer(): # Median pos is an integer number
            median = combined_array[int(pos)]
        else: # Median pos is a float, median is the average of the two middle numbers
            median = (combined_array[floor(pos)] + combined_array[ceil(pos)]) / 2
        return median