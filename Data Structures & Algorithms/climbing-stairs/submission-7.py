class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        def bt(stairs):
            nonlocal res
            if stairs > n:
                return
            if stairs == n:
                res += 1
                return
            
            bt(stairs + 1)
            bt(stairs + 2)
        bt(0)
        return res