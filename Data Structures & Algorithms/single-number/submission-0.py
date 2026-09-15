class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        freq = sorted(freq.items(), key=lambda item: item[1])
        return freq[0][0]