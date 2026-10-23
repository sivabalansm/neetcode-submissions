class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        t = (s + 1) // 2
        memo = {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total >= t or i == len(stones):
                return abs(total - (s - total))
            res = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            memo[(i, total)] = res
            return res
        
        return dfs(0, 0)