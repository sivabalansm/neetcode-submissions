class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in compl:
                return [compl[c], i]
            else:
                compl[nums[i]] = i