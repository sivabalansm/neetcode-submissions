from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        freq_t = dict(Counter(t))
        win = defaultdict(int)

        have = 0
        need = len(freq_t)
        res = [-1, -1]
        size = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in freq_t:
                win[c] += 1
                if win[c] == freq_t[c]:
                    have += 1
            
            while have == need:
                if r - l + 1 < size:
                    res = [l, r]
                    size = r - l + 1
                c = s[l]
                if c in freq_t:
                    if win[c] == freq_t[c]:
                        have -= 1
                    win[c] -= 1
                l += 1

        return s[res[0]:res[1] + 1]
                