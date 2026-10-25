class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        match = Counter(s1)
        win = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                win[s2[l]] -= 1
                if win[s2[l]] == 0:
                    del win[s2[l]]
                l += 1
            
            win[s2[r]] += 1
            if win == match:
                return True
        return False
