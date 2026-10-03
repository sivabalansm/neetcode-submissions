class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        pre[0] = nums[0]
        suf[-1] = nums[-1]

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                res[i] = suf[i + 1]
            elif i == len(nums) - 1:
                res[i] = pre[i - 1]
            else:
                res[i] = pre[i - 1] * suf[i + 1]
        return res