class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        7 6 6 7 8
        7: 0111
        6: 0110
        6: 0110
        7: 0111
        8: 1000
        """
        res = 0
        for n in nums:
            res = n ^ res
        return res