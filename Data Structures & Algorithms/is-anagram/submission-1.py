from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = defaultdict(int)
        for c in s:
            sf[c] += 1

        tf = defaultdict(int)
        for c in t:
            tf[c] += 1
        
        return sf == tf