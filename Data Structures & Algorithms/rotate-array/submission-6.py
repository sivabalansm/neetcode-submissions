class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1234 5678
        4321 8765
        8765 4321
        5678 1234

        12345 678 -> 678 12345

        543 21 876
        678 12345
        """

        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k = k % len(nums)
        l = len(nums) - k
        r = len(nums) - 1
        rev(l, r)
        r = l - 1
        l = 0
        rev(l, r)
        rev(l, len(nums) - 1)
    
