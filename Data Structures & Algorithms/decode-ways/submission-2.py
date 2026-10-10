class Solution:
    def numDecodings(self, s: str) -> int:
        memo = len(s) * [-1]
        def dfs(i):
            nonlocal s
            if i >= len(s) or s[i] == "0":
                return 0
            if memo[i] != -1:
                return memo[i]
            if 0 < int(s[i:i + 2]) <= 26:
                memo[i] = 1 + dfs(i + 2)
            memo[i] = 1 + dfs(i + 1)
            return memo[i]
        return dfs(0)
