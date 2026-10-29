"""
3, 4, 3

2, 9, 8, 3, 6

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if (i, flag) in memo:
                return memo[(i, flag)]

            res = max(nums[i] + dfs(i + 2, flag), dfs(i + 1, flag))
            memo[(i, flag)] = res

            return res
        
        return max(dfs(0, True), dfs(1, False))
            

            


        