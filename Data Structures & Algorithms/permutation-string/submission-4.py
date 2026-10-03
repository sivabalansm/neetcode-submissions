from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1
        print(s1_freq)

        win = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            win[s2[r]] += 1
            if r - l + 1 > len(s1):
                win[s2[l]] -= 1
                if win[s2[l]] == 0:
                    del win[s2[l]]
                l += 1
            if win == s1_freq:
                return True
        return False

