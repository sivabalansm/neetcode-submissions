class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bin(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            return False

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        if nums[l] <= target <= nums[len(nums) - 1]:
            return bin(l, len(nums) - 1)
        else:
            return bin(0, l)
