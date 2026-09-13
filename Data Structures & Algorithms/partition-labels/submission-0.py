class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) < 1:
            return [0]

        # Map char to last index
        lIndex = {}
        for i in range(len(s)):
            lIndex[s[i]] = i

        size, end = 0, 0
        res = []
        for i in range(len(s)):
            size += 1
            char = s[i]
            end = max(end, lIndex[char])
            if i == end:
                res.append(size)
                size = 0
        return res