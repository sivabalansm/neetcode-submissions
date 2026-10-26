class Solution:
    def mySqrt(self, x: int) -> int:


        l = 1
        r = x
        while l <= r:
            m = (l + r) // 2
            s = m ** 2
            if s < x:
                l = m + 1
            elif s > x:
                r = m - 1
            else:
                return m
        return (l + r) // 2