from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        freq_t = dict(Counter(t))
        freq_s = defaultdict(int)
        have, need = 0, len(freq_t)
        res = [-1, -1]
        size = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in freq_t:
                freq_s[c] += 1
                if freq_s[c] == freq_t[c]:
                    have += 1
            
            while have == need:

                if r - l + 1 < size:
                    res = [l, r]
                    size = r - l + 1
                c = s[l]
                if c in freq_t:
                    if freq_s[c] == freq_t[c]:
                        have -= 1
                    freq_s[c] -= 1
                l += 1
        return s[res[0]:res[1] + 1]

            

