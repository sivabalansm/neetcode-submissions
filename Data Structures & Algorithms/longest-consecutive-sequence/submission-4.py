class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsS = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numsS:
                # start of cons seq
                count = 0
                while num + count in numsS:
                    count += 1
                    res = max(res, count)
        
        return res