class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, rem):
            if i >= len(coins) or rem < 0:
                return 0
            if rem == 0:
                return 1
            if (i, rem) in memo:
                return memo[(i, rem)]
            res = dfs(i, rem - coins[i])
            res += dfs(i + 1, rem)
            memo[(i, rem)] = res
            return res
        return dfs(0, amount)

