class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = 0
        for num in nums:
            if curr + num < num:
                curr = num
            else:
                curr += num
            best = max(best, curr)
        return best
