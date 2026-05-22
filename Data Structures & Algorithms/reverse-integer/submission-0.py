class Solution:
    def reverse(self, x: int) -> int:
        RANGE = [-(2**31), 2**31 - 1]

        if not (RANGE[0] <= x <= RANGE[1]):
            return 0

        num = abs(x)
        revNum = 0
        while num > 0:
            lastDigit = num % 10
            revNum = (revNum * 10) + lastDigit
            num = num // 10
        if not (RANGE[0] <= revNum <= RANGE[1]):
            return 0
        return revNum if x >= 0 else -revNum
        
        