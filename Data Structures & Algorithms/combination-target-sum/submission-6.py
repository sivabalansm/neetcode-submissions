class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, arr, acc):
            if i >= len(nums):
                if acc == target:
                    res.append(arr.copy())
                return
            if acc > target:
                return
                
            bt(i + 1, arr, acc)
            arr.append(nums[i])
            bt(i, arr, acc + nums[i])
            arr.pop()
        
        bt(0, [], 0)
        return res