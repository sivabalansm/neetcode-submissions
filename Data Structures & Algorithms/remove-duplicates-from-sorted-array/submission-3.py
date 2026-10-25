class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        2 2 3 3 3 4 4
        l
            r
        """
        n = len(nums)
        l = r = 0
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1
        return l
