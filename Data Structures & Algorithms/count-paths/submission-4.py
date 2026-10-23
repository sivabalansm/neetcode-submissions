class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * m
        dp[-1] = 1
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if j + 1 < m:
                    dp[j] = dp[j + 1] + dp[j]
        return dp[0]