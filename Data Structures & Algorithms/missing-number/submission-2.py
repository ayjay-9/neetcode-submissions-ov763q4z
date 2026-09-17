class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for num in range(len(nums)):
            if num not in nums:
                return num
        return max(nums)+1