from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        win = defaultdict(int)
        for r in range(len(s)):
            win[s[r]] += 1

            while (r - l + 1) - max(win.values()) > k:
                win[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            