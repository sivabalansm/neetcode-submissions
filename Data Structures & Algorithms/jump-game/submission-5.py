class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if i + num >= start:
                start = i
        return start == 0