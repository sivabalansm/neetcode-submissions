class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for i in range(len(nums)):
            n = nums[i]

            if target - n in compl:
                return [compl[target - n], i]
            
            compl[n] = i
        return []