class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_end = max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == current_end:  # exhausted this jump's range — must jump now
                jumps += 1
                current_end = max_reach
        return jumps # minimum number of jumps