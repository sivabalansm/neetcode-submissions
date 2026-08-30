class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            while r - l + 1 - max(count.values())> k:
                count[nums[l]] -= 1
                l += 1
             
            res = max(r - l + 1, res)
        return res

