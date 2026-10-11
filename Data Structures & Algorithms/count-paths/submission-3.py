class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (m + 1)
        dp[m - 1] = 1
        for i in range(n):
            for j in range(m - 1, -1, -1):
                dp[j] = dp[j] + dp[j + 1]
        return dp[0]
