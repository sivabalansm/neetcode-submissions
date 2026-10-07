class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, pos):
            nonlocal res
            if pos == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(pos, len(curr)):
                curr[pos], curr[i] = curr[i], curr[pos]
                bt(curr, pos + 1)
                curr[pos], curr[i] = curr[i], curr[pos]
        bt(nums, 0)
        return res

        