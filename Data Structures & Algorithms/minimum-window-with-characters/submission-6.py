from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        t_freq = dict(Counter(t))

        win_freq = defaultdict(int)
        have, need = 0, len(t_freq)

        res = ""
        size = float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] in t_freq:
                win_freq[s[r]] += 1

                if win_freq[s[r]] == t_freq[s[r]]:
                    have += 1

            while have == need:
                if size > r - l + 1:
                    size = r - l + 1
                    res = s[l:r + 1]
                if s[l] in t_freq:
                    if win_freq[s[l]] == t_freq[s[l]]:
                        have -= 1
                    win_freq[s[l]] -= 1
                l += 1
        return res


