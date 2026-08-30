class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canFit(size):
            subArray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > size:
                    subArray += 1
                    curSum = num
                    if subArray > k:
                        return False
            return True

        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canFit(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res