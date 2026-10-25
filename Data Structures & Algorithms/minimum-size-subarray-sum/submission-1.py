class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        win = 0
        l = 0
        for r in range(len(nums)):
            win += nums[r]
            while win >= target:
                res = min(res, r - l + 1)
                win -= nums[l]
                l += 1

        return res if res != float("inf") else 0
