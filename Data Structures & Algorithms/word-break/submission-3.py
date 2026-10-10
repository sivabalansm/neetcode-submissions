class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lw = len(max(wordDict, key = len))
        wordDict = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(1, lw + 1):
                if s[i : i + j] in wordDict:
                    if dfs(i + j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
        
