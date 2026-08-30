class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        def dfs(i, j, k):
            if k == len(s3):
                return True

            if s1[i] == s3[k]:
                return dfs(i + 1, j, k + 1)
            elif s2[j] == s3[k]:
                return dfs(i, j + 1, k + 1)
            else:
                return False
        return dfs(0, 0, 0)
            

            
