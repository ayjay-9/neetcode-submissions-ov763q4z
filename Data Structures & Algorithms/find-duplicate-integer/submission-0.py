class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l, r = 0, 1
        while l <= r:
            if nums[l] != nums[r]:
                l+=1
                r+=1
            else:
                return nums[l]