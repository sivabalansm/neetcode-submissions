class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # size of sliding window - biggest frequency = what you can replace (to maximize length)
            # k is max quantity replacements, so if it is greater than k, shorten it until it is atleast k
            # that is what this loop is for
            while r - l + 1  - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # "l" has been corrected by the above
            #  So sliding window is placed such that sliding window length - max frequency = residual replaceable -> is less than or equal to k
            res = max(res, r - l + 1)
        return res