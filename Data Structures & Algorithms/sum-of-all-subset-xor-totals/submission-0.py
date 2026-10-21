class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def bt(i, acc):
            nonlocal res
            if i >= len(nums):
                res += acc
                return
            
            bt(i + 1, acc)
            bt(i + 1, acc ^ nums[i])
        
        bt(0, 0)
        return res
