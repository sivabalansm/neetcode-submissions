class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        ba = [False] * n
        def bt(arr):
            nonlocal res
            if len(arr) == n:
                res.append(arr.copy())
                return
            
            for i in range(n):
                if not ba[i]:
                    ba[i] = True
                    arr.append(nums[i])
                    bt(arr)
                    arr.pop()
                    ba[i] = False
        bt([])
        return res
            

