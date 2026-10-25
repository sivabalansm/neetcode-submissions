class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        """
        -1, -1, 0, 1, 2, 4
         k   i           j

        """
        res = []
        for k, a in enumerate(nums):
            #print(k, i, j)
            if a > 0:
                break
            
            if k > 0 and a == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[i] + nums[j] + a

                #print(nums[i], nums[j], nums[k], s)
                if s > 0:
                    j -= 1
                elif s < 0:
                    i += 1
                else:
                    res.append([nums[i], nums[j], a])
                    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                        i += 1
                    i += 1
        return res
                

