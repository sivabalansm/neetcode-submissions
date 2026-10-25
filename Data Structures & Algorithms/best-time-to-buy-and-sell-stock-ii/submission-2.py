class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy = True):
            if i >= len(prices):
                return 0
            
            if (i, buy) in memo:
                return memo[(i, buy)]
            res = 0
            if buy:
                res = max(res, - prices[i] + dfs(i + 1, not buy))
            else:
                res = max(res, prices[i] + dfs(i + 1, not buy))

            res = max(res, dfs(i + 1, buy))
            memo[(i, buy)] = res
            return res
        
        return dfs(0)