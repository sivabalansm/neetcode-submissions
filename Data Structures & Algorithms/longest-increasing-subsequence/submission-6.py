"""
9,1,4,2,3,3,7

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i):
            if i in memo:
                return memo[i]
            lis = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis = max(lis, 1 + dfs(j))
            memo[i] = lis
            return lis
        
        return max(dfs(i) for i in range(n))
                
