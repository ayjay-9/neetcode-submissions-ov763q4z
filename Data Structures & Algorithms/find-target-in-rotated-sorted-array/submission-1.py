class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start+end) // 2
            if target == nums[mid]:
                return mid
            # Left sorted portion
            if nums[start] <= nums[mid]:
                if target > nums[mid] or target < nums[start]: # Go to right portion
                    start = mid+1
                else: # Eliminate right portion
                    end = mid-1
            else: # Right sorted portion
                if target < nums[mid] or target > nums[end]: # Go to left portion
                    end = mid-1
                else:
                    start = mid+1
        return -1