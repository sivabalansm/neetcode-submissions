class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        best = nums[0]

        for num in nums:
            if num > curr + num:
                curr = 0
            curr += num
            best = max(best, curr)
        return best