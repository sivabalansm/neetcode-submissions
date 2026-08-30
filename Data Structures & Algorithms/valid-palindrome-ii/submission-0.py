class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        delete = False
        while l < r:

            if not delete and s[l] != s[r]:
                delete = True
            elif s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
