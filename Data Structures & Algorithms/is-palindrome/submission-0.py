class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:

            while not (('a' <= s[i] and s[i] <= 'z') or ('A' <= s[i] and s[i] <= 'Z') or ('0' <= s[i] and s[i] <= '9')):
                i += 1
                
            while not (('a' <= s[j] and s[j] <= 'z') or ('A' <= s[j] and s[j] <= 'Z') or ('0' <= s[j] and s[i] <= '9')):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            
