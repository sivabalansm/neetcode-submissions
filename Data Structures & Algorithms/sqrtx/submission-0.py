import math
class Solution:
    def mySqrt(self, x: int) -> int:


        l = 0
        r = math.ceil(x / 2)
        while l <= r:
            m = (l + r) // 2
            s = m * m

            if s > x:
                r = m - 1
            elif s < x:
                l = m + 1
            else:
                return m
        return l - 1