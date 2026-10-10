class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}
        def dfs(i, acc):
            if i >= len(nums):
                return False
            if (i, acc) in memo:
                return memo[(i, acc)]

            if dfs(i + 1, acc) or dfs(i + 1, acc + nums[i]):
                return True

            if acc == total - acc:
                memo[(i, acc)] = True
                return True
            memo[(i, acc)] = False
            return False
            
        return dfs(0, 0)
