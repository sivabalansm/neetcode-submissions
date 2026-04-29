class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for i in range(len(nums)):
            num = nums[i]

            if target - num in compl:
                return [compl[target - num], i]
            else:
                compl[num] = i
        return []