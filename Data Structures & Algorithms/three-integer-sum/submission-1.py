class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for t in range(len(nums) - 1, 1, -1):
            l = 0
            r = t - 1
            if t > 2 and nums[t] == nums[t-1]:
                continue
            target = -nums[t]

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], -target])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
