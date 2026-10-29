"""


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n : 1}
        def dfs(i):
            if i > n:
                return 0
            if i in memo:
                return memo[i]

            res = 0
            res += dfs(i + 1)
            res += dfs(i + 2)
            
            memo[i] = res
            return res
        return dfs(0)
