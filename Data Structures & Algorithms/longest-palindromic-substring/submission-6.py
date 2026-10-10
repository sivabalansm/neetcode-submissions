from functools import lru_cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        @lru_cache(maxsize=None)
        def isPal(i: int, j: int) -> bool:
            if j - i <= 1:                 # length 1 or 2 (or empty inner part)
                return s[i] == s[j]
            if s[i] != s[j]:
                return False
            return isPal(i + 1, j - 1)

        resIdx, resLen = 0, 0
        for i in range(n):
            for j in range(i, n):
                if isPal(i, j) and resLen < (j - i + 1):
                    resIdx = i
                    resLen = j - i + 1

        return s[resIdx : resIdx + resLen]