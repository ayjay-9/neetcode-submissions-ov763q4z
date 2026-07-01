class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = sorted(set(nums))
        count = 1
        sequence = []

        if not nums:
            return 0
        
        if len(ordered_nums) == 1:
            return count

        for i in range(len(ordered_nums) - 1):
            if (ordered_nums[i + 1] == ordered_nums[i] + 1):
                count = count + 1
            else:
                sequence.append(count)
                count = 1
                continue
            sequence.append(count) # If everything is in sequence
        return max(sequence)