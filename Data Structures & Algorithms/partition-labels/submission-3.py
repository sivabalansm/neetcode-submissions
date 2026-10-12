class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        
        last_idx = {}

        for i in range(len(s)):
            last_idx[s[i]] = i
        res = []
        nidx = last_idx[s[0]]
        prev = -1
        for i in range(len(s)):
            nidx = max(nidx, last_idx[s[i]])
            if i == nidx:
                res.append(nidx - prev)
                prev = nidx
        return res