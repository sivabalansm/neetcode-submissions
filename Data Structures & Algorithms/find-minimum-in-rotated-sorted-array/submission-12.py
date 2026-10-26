"""
3,4,5,6,1,2
l         r
    m


6 1 2 3 4 5
l         r
    m

4 5 0 1 2 3
l   m     r

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        return nums[l - 1]
