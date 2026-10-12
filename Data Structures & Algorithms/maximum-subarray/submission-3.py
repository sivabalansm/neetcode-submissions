class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        for num in nums[1:]:
            if curr + num < num:
                curr = num
            else:
                curr += num
            best = max(best, curr)
        return best