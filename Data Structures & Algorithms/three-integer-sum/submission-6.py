class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        """
        -4, -1, -1, 0, 1, 2
        l              r  R
        """

        for i in range(len(nums) - 1, -1, -1):
            target = -nums[i]

            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], -target])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1
                    while r - 1 > 0 and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                
        return res

