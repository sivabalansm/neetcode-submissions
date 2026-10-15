class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        res = 1
        isNeg = True if n < 0 else False
        n = abs(n)
        while n > 0:
            res *= x
            n -= 1
        return res if not isNeg else 1/res