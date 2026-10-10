class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i, prev):
            if i == len(nums):
                return 0

            #if memo[i] != -1:
            #    return memo[i]

            att1 = 0
            att2 = 0
            if nums[i] > prev:
                att1 = 1 + dfs(i + 1, nums[i])
            att2 = dfs(i + 1, prev) 
            res = max(att1, att2)
            memo[i] = res
            return res
        return dfs(0, -1)
        