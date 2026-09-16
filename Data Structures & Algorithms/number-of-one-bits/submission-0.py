class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(format(n, "b"))
        count = 0
        for bit in binary:
            if int(bit) ^ 1 == 0:
                count += 1
        return count