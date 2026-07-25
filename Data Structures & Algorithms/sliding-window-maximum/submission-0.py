class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num = []
        left = 0
        window = []
        for right in range(k-1, len(nums)):
            window = nums[left:right+1]
            max_num.append(max(window))
            left += 1
        return max_num