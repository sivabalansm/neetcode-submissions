class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            skip = dfs(i + 1, buying)
            res = 0
            if buying:
                res = dfs(i + 1, not buying) - prices[i]
            else:
                res = dfs(i + 2, not buying) + prices[i]
            memo[(i, buying)] = max(skip, res)
            return memo[(i, buying)]
        return dfs(0, True)