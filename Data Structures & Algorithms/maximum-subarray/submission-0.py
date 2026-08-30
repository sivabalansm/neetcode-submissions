class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        rs = sum(nums)
        crs = rs
        while l < r:
            if nums[l] < nums[r]:
                crs = crs - nums[l]
                l += 1
            else:
                crs = crs - nums[r]
                r -= 1

            rs = max(crs, rs)
        return rs
