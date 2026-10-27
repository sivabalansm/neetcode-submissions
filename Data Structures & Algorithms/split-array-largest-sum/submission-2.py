class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(limit):
            subarray = 1
            curr = 0
            for num in nums:
                if curr + num > limit:
                    curr = 0
                    subarray += 1
                    if subarray > k:
                        return False
                curr += num
            return True
            


        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
                