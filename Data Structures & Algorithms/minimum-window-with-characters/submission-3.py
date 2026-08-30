from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = dict(Counter(t))

        win_freq = defaultdict(int)
        res = ""
        size = float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] in t_freq:
                win_freq[s[r]] += 1
            
            while win_freq == t_freq:
                if size > r - l + 1:
                    size = r - l + 1
                    res = s[l:r + 1]
                if s[l] in t_freq:
                    win_freq[s[l]] -= 1
                if win_freq[s[l]] == 0:
                    del win_freq[s[l]]
                l += 1
        return res


