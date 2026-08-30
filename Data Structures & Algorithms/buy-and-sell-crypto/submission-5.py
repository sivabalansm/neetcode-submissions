class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        """
        10 1 5 6 7 1
        l  r
        """

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(profit, res)
            else:
                l = r
        return res



