class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for bit in range(n+1):
            count = 0
            while bit:
                bit &= bit-1
                count += 1
            res.append(count)
        return res