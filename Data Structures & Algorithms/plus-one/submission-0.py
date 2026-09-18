class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        num = str(int(num)+1)
        res = []
        for n in num:
            res.append(int(n))
        return res