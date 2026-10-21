class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []
        curr = []
        wordDict = set(wordDict)

        def bt(i):
            nonlocal res
            if i >= len(s):
                res.append(" ".join(curr))
                return 
            
            for j in range(i, n):
                if s[i:j + 1] in wordDict:
                    curr.append(s[i:j+1])
                    bt(j + 1)
                    curr.pop()
        
        bt(0)
        return res