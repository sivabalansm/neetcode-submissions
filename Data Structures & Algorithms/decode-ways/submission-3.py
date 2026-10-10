class Solution:
    def numDecodings(self, s: str) -> int:
        memo = len(s) * [-1]

        def dfs(i):
            nonlocal s
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                memo[i] += dfs(i + 2)
            return memo[i]
        return dfs(0)
