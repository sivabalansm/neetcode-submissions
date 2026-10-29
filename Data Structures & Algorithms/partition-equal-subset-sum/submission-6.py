class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total / 2
        memo = {}
        def dfs(i, acc):
            if i >= len(nums):
                memo[(i, acc)] = False
                return False
            
            if acc > target:
                memo[(i, acc)] = False
                return False
            
            if acc == target:
                memo[(i, acc)] = True
                return True
            
            if (i, acc) in memo:
                return memo[(i, acc)]
            
            if dfs(i + 1, acc) or dfs(i + 1, acc + nums[i]):
                memo[(i, acc)] = True
                return True
            
            memo[(i, acc)] = False
            return False
        
        return dfs(0, 0)
            
            
