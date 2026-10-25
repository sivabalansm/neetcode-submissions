class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        pre[0] = nums[0]
        suf[-1] = nums[-1]
        for i in range(1, len(nums)):
            pre[i] = nums[i] * pre[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = nums[i] * suf[i + 1]
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suf[i + 1])
            elif i == len(nums) - 1:
                res.append(pre[i - 1])
            else:
                res.append(pre[i - 1] * suf[i + 1])
        return res