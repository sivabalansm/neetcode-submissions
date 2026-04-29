class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 101
        mp = 0

        for v in prices:
            mp = max(mp, v - b)
            b = min(b, v) 

        return mp
        