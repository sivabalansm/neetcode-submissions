from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = [0] * 26
        ta = [0] * 26

        for c in s:
            sa[ord(c) - ord('a')] += 1

        for c in t:
            ta[ord(c) - ord('a')] += 1
        
        if sa == ta:
            return True
        return False 
        