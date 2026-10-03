class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for i, n in enumerate(nums):

            if n in compl:
                return [compl[n], i]
            
            compl[target - n] = i
        return []