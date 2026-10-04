class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        3 4 5 6 1 2
              l m r
        """

        l = 0
        r = len(nums) - 1
        res = nums[l]
        if nums[l] < nums[r] or len(nums) == 1:
            return res

        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                r = m - 1
        res = min(res, nums[l])
        return res


