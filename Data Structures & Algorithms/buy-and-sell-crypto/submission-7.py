class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        10 1 5 6 7 1
           l   
        """

        l = 0
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - prices[l])
            if prices[i] < prices[l]:
                l = i
        return res