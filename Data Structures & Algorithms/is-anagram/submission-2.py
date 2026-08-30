class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ars = [0] * 26
        art = [0] * 26
        for c in s:
            ars[ord(c) - ord("a")] += 1
        
        for c in t:
            art[ord(c) - ord("a")] += 1
        
        return ars == art
