class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l = 0
       mp = 0

       for r in range(len(prices)):
            if not prices[l] < prices[r]:
                l = r
                continue
            p = prices[r] - prices[l]
            mp = max(mp, p)
       return mp
        

            

