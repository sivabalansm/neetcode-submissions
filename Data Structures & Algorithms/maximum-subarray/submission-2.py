class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            if num > curr:
                curr = num
            else:
                curr += num
        return curr