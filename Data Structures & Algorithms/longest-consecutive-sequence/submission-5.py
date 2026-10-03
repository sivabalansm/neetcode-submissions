class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        res = 0
        for num in nums:

            if num - 1 not in ns:
                # num cons start
                cnt = 0
                while num in ns:
                    cnt += 1
                    num += 1
                
                res = max(res, cnt)
        return res


