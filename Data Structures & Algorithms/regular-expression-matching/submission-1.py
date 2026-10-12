class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in memo:
                return memo[(i, j)]

            m = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                if (m and dfs(i + 1, j)) or dfs(i, j + 2):
                    memo[(i, j)] = True
                    return True
            if m:
                res = dfs(i + 1, j + 1)
                memo[(i, j)] = res
                return res
            
            memo[(i, j)] = False
            return False
        return dfs(0, 0)