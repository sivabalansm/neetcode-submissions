class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i
        
        count = 0
        nextIdx = 0
        res = []
        for i in range(len(s)):
            c = s[i]
            nextIdx = max(nextIdx, lastIdx[c])
            count += 1
            if i == nextIdx:
                res.append(count)
                count = 0
        return res