class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ba = [False] * n
        res = set()
        def bt(arr):
            nonlocal res
            if len(arr) == n:
                res.add(tuple(arr.copy()))
                return
            
            for i in range(n):
                if not ba[i]:
                    ba[i] = True
                    arr.append(nums[i])
                    bt(arr)
                    arr.pop()
                    ba[i] = False
        bt([])
        return list(res)
