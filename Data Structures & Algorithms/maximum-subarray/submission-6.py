class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        for num in nums[1:]:
            if num + curr < num:
                curr = 0
            curr += num
            best = max(curr, best)
        return best


