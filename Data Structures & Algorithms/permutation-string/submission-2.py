class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1fq = {}
        for c in s1:
            s1fq[c] = s1fq.get(c, 0) + 1
        
        wfq = {}
        l = 0
        for r in range(len(s2)):
            wfq[s2[r]] = wfq.get(s2[r], 0) + 1

            while len(s1) < r - l + 1:
                wfq[s2[l]] -= 1
                if wfq[s2[l]] <= 0:
                    del wfq[s2[l]]
                l += 1
            
            if wfq == s1fq:
                return True

        return False