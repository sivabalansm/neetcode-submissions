class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sn = set()
        ml = 0
        l = 0

        for r in range(len(s)):
            while s[r] in sn:
                sn.remove(s[l])
                l += 1
            sn.add(s[r])

            ml = max(r - l + 1, ml)
        return ml


        