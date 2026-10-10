class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        res = False
        def dfs(i, acc):
            nonlocal res
            if i >= len(nums):
                return 0
            
            dfs(i + 1, acc)
            dfs(i + 1, acc + nums[i])
            if acc == total - acc:
                res = True
            
        dfs(0, 0)
        return res
