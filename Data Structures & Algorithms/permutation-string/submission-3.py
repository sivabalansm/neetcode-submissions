from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        match_freq = dict(Counter(s1))
        print(match_freq)
        freq = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            freq[s2[r]] += 1
            if r - l + 1 > len(s1):
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    del freq[s2[l]]
                l += 1
            print(freq)
            if freq == match_freq:
                return True
        return False



        
        