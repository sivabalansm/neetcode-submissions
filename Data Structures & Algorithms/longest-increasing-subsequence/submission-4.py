class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            att1 = 0
            att2 = 0
            if nums[i] > prev:
                att1 = 1 + dfs(i + 1, nums[i])
            att2 = dfs(i + 1, prev) 
            res = max(att1, att2)
            memo[(i, prev)] = res
            return res
        return dfs(0, float("-inf"))
        