class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        """
        1 : 0001
        2 : 0010
          : 0011
        3 : 0011
          : 0000
        4 : 0100
          : 0100
        5 : 0101
          : 0001
        6 : 0110
          : 0111
        7 : 0111
        0 : 0000
        """
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        res ^= len(nums)
        return res
        

