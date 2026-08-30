class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(k, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1