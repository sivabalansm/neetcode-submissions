class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        one = nums[0]
        two = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = two
            two = max(two, nums[i] + one)
            one = tmp
        return two