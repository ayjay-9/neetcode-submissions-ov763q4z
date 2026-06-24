class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I'll need the number and the count
        groups = defaultdict(int) # Number: 0 by default

        for num in sorted(nums):
            groups[num] += 1
        
        return list(sorted(groups, key=groups.get, reverse=True)[0:k])