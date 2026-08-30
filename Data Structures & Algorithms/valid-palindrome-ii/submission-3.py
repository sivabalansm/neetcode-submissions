class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 2:
            return True
        l = 0
        r = len(s) - 1

        delete = False
        while l < r:

            if not delete and s[l] != s[r]:
                if s[l + 1] == s[r]:
                    l += 1
                    delete = True
                elif s[l] == s[r - 1]:
                    r -= 1
                    delete = True
                else:
                    return False
            elif s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
