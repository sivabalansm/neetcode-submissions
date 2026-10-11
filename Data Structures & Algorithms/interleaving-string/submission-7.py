class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(p1, p2, p3):
            if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
                return True
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            res = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                if dfs(p1 + 1, p2, p3 + 1):
                    res = True
            
            if not res and p2 < len(s2) and s2[p2] == s3[p3]:
                if dfs(p1, p2 + 1, p3 + 1):
                    res = True
            memo[(p1, p2)] = res
            return res
        return dfs(0, 0, 0)
