class Solution:
    def integerBreak(self, n: int) -> int:
        memo = { 0 : 1 }
        def dfs(total):
            if total in memo:
                return memo[total]
            res = 1
            for i in range(1, total + 1):
                #print(i)
                if total < i:
                    break
                res = max(res, i * dfs(total - i))
                #print(res)
            memo[total] = res
            return res

        return dfs(n)