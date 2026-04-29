class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)

        for i in range(len(nums)):
            prev = pre[i - 1] if i > 0 else 1
            pre[i] = prev * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            bef = suf[i + 1] if i < len(nums) - 1 else 1
            suf[i] = bef * nums[i]
        print(pre)
        print(suf)
        res = []
        for i in range(len(nums)):
            prev = pre[i - 1] if i > 0 else 1
            next = suf[i + 1] if i < len(nums) - 1 else 1
            res.append(prev * next)
        return res