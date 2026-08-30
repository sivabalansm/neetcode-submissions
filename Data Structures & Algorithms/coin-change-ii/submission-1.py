class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            
            if (i, total) in dp:
                return dp[(i, total)]
            res = 0
            res += dfs(i, total + coins[i])
            res += dfs(i + 1, total)

            dp[(i, total)] = res

            return res
        return dfs(0, 0)
