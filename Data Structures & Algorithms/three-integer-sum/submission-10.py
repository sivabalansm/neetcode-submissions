class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for t in range(len(nums)):
            target = nums[t]

            if target >= 0:
                break
            
            if t > 0 and nums[t] == nums[t - 1]:
                continue

            l = t + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + target

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], target])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res