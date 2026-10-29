class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            res = 0
            res = max(res, dfs(i + 1, prev))
            if prev < nums[i]:
                res = max(res, 1 + dfs(i + 1, nums[i]))
            memo[(i, prev)] = res
            return res
        
        return dfs(0, float("-inf"))


            