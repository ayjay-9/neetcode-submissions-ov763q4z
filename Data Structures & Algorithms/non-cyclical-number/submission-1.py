class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n:
            digits = [digit for digit in str(n)]
            sum = 0
            for i in range(len(digits)):
                sum += int(digits[i])**2
            if sum == 1:
                return True
            else:
                if sum in seen:
                    return False
                seen.add(sum)
                n = sum
        return False