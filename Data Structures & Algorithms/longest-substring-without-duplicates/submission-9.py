class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        sn = set()
        l = 0
        sn
        for r in range(len(s)):
            while s[r] in sn:
                sn.remove(s[l])
                l += 1
            sn.add(s[r])
            res = max(res, r - l + 1)
        return res