class Solution:
    def numSquares(self, n: int) -> int:
        half = int(n ** 0.5)
        memo = {}
        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]

            res = float("inf")
            for num in range(half + 1, 0, -1):
                if total < num ** 2:
                    continue
                res = min(res, 1 + dfs(total - num ** 2))

            memo[total] = res
            return res
        return dfs(n)
        