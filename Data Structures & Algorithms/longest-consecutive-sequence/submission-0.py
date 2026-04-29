class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = set(nums)
        res = 0
        for n in nums:
            c = 0
            if n-1 not in sn:
                while n in sn:
                    c += 1
                    n += 1
            res = max(res, c)
        return res



        