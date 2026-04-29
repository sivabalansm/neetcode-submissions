class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(i, sub, total):
            if total == target:
                res.add(tuple(sub.copy()))
            if i >= len(nums) or total > target:
                return
            
            sub.append(nums[i])
            dfs(i, sub, total + nums[i])
            sub.pop()
            dfs(i + 1, sub, total)
        dfs(0, [], 0)
        return [list(e) for e in res]
            