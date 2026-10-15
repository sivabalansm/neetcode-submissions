class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        isNeg = True if n < 0 else False
        n = abs(n)
        while n > 0:
            res *= x
            n -= 1
        return res if not isNeg else 1/res