class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        self.resLen = 0
        self.res = [-1, -1]
        def pal_check(l, r):
            while l > 0 and r < len(s) - 1 and s[l] == s[r]:
                if r - l + 1 > self.resLen:
                    self.res = [l, r]
                    self.resLen = r - l + 1
                l -= 1
                r += 1

        for c in range(len(s)):
            if c > 0 and c < len(s) - 1:

                pal_check(c - 1, c + 1)

                if c + 1 < len(s) and s[c] == s[c + 1]:
                    pal_check(c, c+1)
                
                if c - 1 > 0 and s[c-1] == s[c]:
                    pal_check(c - 1, c)
        
        return s[self.res[0]: self.res[1] + 1]
