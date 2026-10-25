class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(len(nums) - 1, -1, -1):
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue

                if i >= j:
                    break

                l = i + 1
                r = j - 1
                while l < r:
                    s = nums[l] + nums[r] + nums[i] + nums[j]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[l], nums[r], nums[i], nums[j]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        
        return res

                    