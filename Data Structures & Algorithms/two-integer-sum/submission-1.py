class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in c:
                return [c[comp], i]
            c[nums[i]] = i
        return -1
            