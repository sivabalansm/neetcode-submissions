class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canFit(numSize):
            subarr = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > numSize:
                    curSum = num
                    subarr += 1
                    if subarr > k:
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