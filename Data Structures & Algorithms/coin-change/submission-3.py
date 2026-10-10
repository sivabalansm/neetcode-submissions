class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            memo = {}
            def dfs(amount):
                if amount == 0:
                    return 0

                if amount in memo:
                    return memo[amount]

                memo[amount] = 1e9
                for coin in coins:
                    if amount - coin >= 0:
                        memo[amount] = min(memo[amount], 1 + dfs(amount - coin))
                return memo[amount]
            res = int(dfs(amount))
            return res if res != 1e9 else -1
            

            

