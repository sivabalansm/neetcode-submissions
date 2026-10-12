class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                break
            reach = max(reach, nums[i] + i)
        return reach >= len(nums) - 1
