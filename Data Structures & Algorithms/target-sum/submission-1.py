class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            n = nums[i]
            res = 0
            res = dfs(i + 1, total + n)
            res += dfs(i + 1, total - n)

            memo[(i, total)] = res

            return res
        return dfs(0, 0)



