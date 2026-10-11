class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, acc):
            if i >= len(nums):
                return acc == target
            if (i, acc) in memo:
                return memo[(i, acc)]
            res = dfs(i + 1, acc + nums[i])
            res += dfs(i + 1, acc - nums[i])
            memo[(i, acc)] = res
            return res
        
        return dfs(0, 0)

            
