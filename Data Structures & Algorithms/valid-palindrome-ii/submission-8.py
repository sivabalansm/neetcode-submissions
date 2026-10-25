class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        skip = False
        while l < r:
            if s[l] != s[r] and not skip:
                skip = True
                if s[l + 1] == s[r]:
                    l += 1
                elif s[r - 1] == s[l]:
                    r -= 1
                else:
                    return False
            elif s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

