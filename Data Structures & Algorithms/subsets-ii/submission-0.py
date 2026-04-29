class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sub = []

        def dfs(i):
            if i >= len(nums):

                res.add(tuple(sorted(sub.copy())))
                return
            sub.append(nums[i]) 
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        dfs(0)

        return [list(e) for e in res]
