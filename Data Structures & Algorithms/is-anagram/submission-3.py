from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)

        for c in s:
            sd[c] += 1
        for c in t:
            td[c] += 1
        
        for c in sd:
            if sd[c] != td[c]:
                return False

        for c in td:
            if sd[c] != td[c]:
                return False
        return True