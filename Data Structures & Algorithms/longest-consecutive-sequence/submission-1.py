class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lu = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in lu:
                count = 0
                while count + n in lu:
                    res = max(count, res)
                    count += 1
        return res + 1