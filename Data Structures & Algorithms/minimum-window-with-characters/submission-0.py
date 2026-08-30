class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        fqt = {}
        for c in t:
            fqt[c] = fqt.get(c, 0) + 1

        fq = {}
        res = s
        for r in range(len(s)):
            if s[r] in fqt:
                fq[s[r]] = fq.get(s[r], 0) + 1
            while fq.keys() == fqt.keys():
                if s[l] in fq:
                    fq[s[l]] -= 1
                    if fq[s[l]] <= 0:
                        del fq[s[l]]
                res = min(s[l:r], res)
                l += 1
        return res
            


