class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_seen = 1
        max_seen = 1
        dp = [nums[0]] * (len(nums)+1)

        for i, n in enumerate(nums):
            tmp = n * max_seen
            max_seen = max(n, tmp, n * min_seen)
            min_seen = min(n, tmp, n * min_seen)
            dp[i] = max(max_seen, dp[i-1])
        print(dp[-2])

        return dp[-2]
        """
        2 4 -3 5
               i
        tmp = -120
        mas = 5
        mis = -120
        dp = [2, 8,]
        """