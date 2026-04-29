class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums) 
        suf = [1] * len(nums)

        for i in range(len(nums)):
            pre[i] = nums[i] * pre[i -1]
        
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = nums[i] * suf[i + 1] if i < len(nums) - 1 else nums[i]
        
        res = []
        pre = [1] + pre 
        suf = suf + [1]
        for i in range(len(nums)):
            res.append(pre[i ] * suf[i + 1])
        return res


