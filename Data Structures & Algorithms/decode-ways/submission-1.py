class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            nonlocal s
            if i >= len(s) or s[i] == "0":
                return 0
            su = 0
            if 0 < int(s[i:i + 2]) <= 26:
                su = 1 + dfs(i + 2)
            su = 1 + dfs(i + 1)
            return su
        return dfs(0)
