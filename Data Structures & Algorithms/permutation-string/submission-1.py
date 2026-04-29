class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1fq = {}
        for c in s1:
            s1fq[c] = s1fq.get(c, 0) + 1

        s2fq = {}

        l = 0
        for r in range(len(s2)):
            s2fq[s2[r]] = s2fq.get(s2[r], 0) + 1

            while r - l >= len(s1):
                s2fq[s2[l]] -= 1
                if s2fq[s2[l]] == 0:
                    del s2fq[s2[l]]
                    
                l += 1
            
            if s2fq == s1fq:
                return True

        return False
            
            



        