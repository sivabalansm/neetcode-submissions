class Solution:
    def climbStairs(self, n: int) -> int:
        def bt(x):
            if x >= n:
                return x == n
            return bt(x + 1) + bt(x + 2)
        return bt(0)
                