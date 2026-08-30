class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        def bt(x):
            if x > n:
                return
            elif x < n:
                bt(x + 1)
                bt(x + 2)
            else:
                self.res += 1
        bt(0)
        return self.res
                