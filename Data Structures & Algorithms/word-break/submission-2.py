class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lw = len(max(wordDict, key = len))
        def dfs(i):
            if i == len(s):
                return True
            
            for j in range(1, lw + 1):
                if s[i : i + j] in wordDict:
                    if dfs(i + j):
                        return True
            return False
        return dfs(0)
        
