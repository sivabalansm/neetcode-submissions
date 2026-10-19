class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        res = 0
        while i + nums[i] < len(nums) - 1:
            num = nums[i]
            reach_max = (i + num, i)
            for j in range(i + 1, i + num + 1):
                reach_max = max(reach_max, (j + nums[j], j), key=lambda t: t[0])

            i = reach_max[1]
            res += 1
        return res + 1