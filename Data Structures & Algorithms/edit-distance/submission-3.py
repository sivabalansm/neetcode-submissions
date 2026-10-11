class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        def dfs(i, j):
            if i >= len(word1) or j >= len(word2):
                return 0

            res = float("inf")
            if word1[i] == word2[j]:
                res = min(res, dfs(i + 1, j + 1))
            else: 
                res = min(res, 1 + dfs(i + 1, j + 1)) # replace
                res = min(res, 1 + dfs(i, j + 1)) # insert
                res = min(res, 1 + dfs(i + 1, j)) # delete
            
            return res
        return dfs(0, 0) + 1