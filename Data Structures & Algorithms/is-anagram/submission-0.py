class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfq = [0] * 26
        tfq = [0] * 26
        for c in s:
            sfq[ord(c) - ord('a')] += 1
        
        for c in t:
            tfq[ord(c) - ord('a')] += 1
        
        if sfq == tfq:
            return True
        return False