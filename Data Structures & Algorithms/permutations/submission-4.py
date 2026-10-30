class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        boolArr = [False] * len(nums)
        res = []
        arr = []
        def bt():
            nonlocal arr
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for i in range(len(nums)):
                if not boolArr[i]:
                    boolArr[i] = True
                    arr.append(nums[i])
                    bt()
                    arr.pop()
                    boolArr[i] = False
        bt()
        return res
